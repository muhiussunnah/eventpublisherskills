"""Scroll the current list and collect every card (clickable node with 2+ lines).
usage: collect.py OUTNAME [MAXSWIPES]
writes scratchpad/emu/OUTNAME.json (list of card label strings in order)"""
import json
import sys
import time

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import emu  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
name = sys.argv[1]
maxs = int(sys.argv[2]) if len(sys.argv) > 2 else 40
seen = []
same = 0
# go to the top of the list first
for _ in range(int(sys.argv[3]) if len(sys.argv) > 3 else 0):
    emu.adb("shell", "input", "swipe", "540", "800", "540", "2100", "150")
time.sleep(0.9)
for i in range(maxs):
    new = 0
    for lab, x, y, b, cl in emu.nodes():
        if cl == "true" and "&#10;" in lab and 600 < y < 2150 and lab not in seen:
            # skip bottom nav
            if lab.startswith("Hitta på&#10;"):
                continue
            seen.append(lab)
            new += 1
    if new == 0:
        same += 1
        if same >= 2:
            break
    else:
        same = 0
    emu.adb("shell", "input", "swipe", "540", "1900", "540", "900", "500")
    time.sleep(0.9)
os.makedirs(emu.OUT, exist_ok=True)
out = os.path.join(emu.OUT, name + ".json")
json.dump([s.replace("&#10;", " | ").replace("&amp;", "&") for s in seen], open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(seen), "cards ->", out)
for s in seen:
    print(" -", s.replace("&#10;", " | ").replace("&amp;", "&")[:150])
