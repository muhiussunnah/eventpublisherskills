import os, sys, re, datetime
sys.stdout.reconfigure(encoding="utf-8")
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "NORRLAND-GOTLAND-PERMANENT-PLACES-FINAL-REPORT-2026-11-18.md")
DAYS = ["mån", "tis", "ons", "tor", "fre", "lör", "sön"]
rows = []
for ln in open(R, encoding="utf-8").read().split("\n")[43:240]:
    c = [x.strip() for x in ln.split("|")]
    if len(c) < 9 or "→" not in c[5]:
        continue
    reg, kom, name, win, per = c[1], c[2], c[3], c[4], c[5]
    a, b = [datetime.date.fromisoformat(x.strip()) for x in per.split("→")]
    if win.startswith("alla dagar") or win.startswith("alltid"):
        d = set(range(7))
    else:
        d = {i for i, k in enumerate(DAYS) if re.search(r"\b" + k + r"\b", win)}
    rows.append((reg, kom, name, win, a, b, d))
def expect(region, date):
    return [r for r in rows if r[0] == region and r[4] <= date <= r[5] and date.weekday() in r[6]]
if __name__ == "__main__":
    region = sys.argv[1]
    date = datetime.date.fromisoformat(sys.argv[2])
    tot = [r for r in rows if r[0] == region]
    e = expect(region, date)
    print(region, date, date.strftime("%a"), "published:", len(tot), "expected open:", len(e))
    for r in e:
        print("  ", r[1], "|", r[2], "|", r[3])
