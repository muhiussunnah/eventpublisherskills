"""Small adb helper for the famies emulator.
usage:
  emu.py shot NAME            -> scratchpad/emu/NAME.png + NAME_small.jpg (360x800)
  emu.py ui                   -> list visible UI nodes (text / content-desc / bounds)
  emu.py tap X Y              -> tap device pixels (1080x2400)
  emu.py taptext TEXT [N]     -> tap the N-th (default 0) node whose text/desc contains TEXT
  emu.py swipe X1 Y1 X2 Y2 [MS]
  emu.py key KEYCODE
  emu.py geo LAT LNG
  emu.py type TEXT
"""
import os
import re
import subprocess
import sys
import time

ADB = os.environ.get("ADB", os.path.expandvars(r"%LOCALAPPDATA%/Android/Sdk/platform-tools/adb.exe"))
OUT = os.environ.get("EMU_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "out"))


def adb(*a, binary=False):
    r = subprocess.run([ADB, *a], capture_output=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def shot(name):
    from PIL import Image
    import io
    os.makedirs(OUT, exist_ok=True)
    data = adb("exec-out", "screencap", "-p", binary=True)
    p = os.path.join(OUT, name + ".png")
    open(p, "wb").write(data)
    im = Image.open(io.BytesIO(data)).convert("RGB")
    im.resize((360, 800)).save(os.path.join(OUT, name + "_small.jpg"), quality=85)
    print("saved", p)


def nodes():
    adb("shell", "uiautomator", "dump", "/sdcard/ui.xml")
    xml = adb("shell", "cat", "/sdcard/ui.xml")
    res = []
    for m in re.finditer(r"<node [^>]*>", xml):
        n = m.group(0)
        t = re.search(r' text="([^"]*)"', n).group(1)
        d = re.search(r' content-desc="([^"]*)"', n).group(1)
        b = re.search(r' bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        cl = re.search(r' clickable="(\w+)"', n).group(1)
        if (t or d) and b:
            x1, y1, x2, y2 = map(int, b.groups())
            res.append(((t + " | " + d).strip(" |"), (x1 + x2) // 2, (y1 + y2) // 2, (x1, y1, x2, y2), cl))
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    c = sys.argv[1]
    a = sys.argv[2:]
    if c == "shot":
        shot(a[0])
    elif c == "ui":
        for lab, x, y, b, cl in nodes():
            lab = lab.replace("\n", " / ")
            print(f"{x:5d},{y:5d} {'C' if cl == 'true' else ' '} {lab[:160]}")
    elif c == "tap":
        adb("shell", "input", "tap", a[0], a[1])
    elif c == "taptext":
        idx = int(a[1]) if len(a) > 1 else 0
        hits = [n for n in nodes() if a[0].lower() in n[0].lower()]
        if len(hits) <= idx:
            print("NOT FOUND", a[0])
            sys.exit(1)
        lab, x, y, b, cl = hits[idx]
        adb("shell", "input", "tap", str(x), str(y))
        print("tapped", lab[:80].replace("\n", " / "), x, y)
    elif c == "swipe":
        ms = a[4] if len(a) > 4 else "400"
        adb("shell", "input", "swipe", a[0], a[1], a[2], a[3], ms)
    elif c == "key":
        adb("shell", "input", "keyevent", a[0])
    elif c == "geo":
        print(adb("emu", "geo", "fix", a[1], a[0]))
    elif c == "type":
        adb("shell", "input", "text", a[0].replace(" ", "%s"))
    time.sleep(0.3)


if __name__ == "__main__":
    main()
