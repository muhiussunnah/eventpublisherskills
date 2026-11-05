"""Validate fix specs (fixo/f_*.json) against the rules and build apply.json + problems.json."""
import json, glob, re, os, datetime as dt
AUD = r"C:\Users\User\AppData\Local\Temp\claude\793086065a500b32\4ad7473a-f7bd-4184-b47a-6ef00f11c16a\scratchpad\audit"
TODAY = "2026-11-05"; MAXEND = "2027-12-31"
inp = {}
for f in glob.glob(AUD + r"\fixb\f_*.json"):
    for it in json.load(open(f, encoding="utf-8-sig")):
        inp[it["id"]] = it
specs = {}
for f in sorted(glob.glob(AUD + r"\fixo\f_*.json")) + sorted(glob.glob(AUD + r"\fixo2\*.json")):
    try:
        arr = json.load(open(f, encoding="utf-8-sig"))
    except Exception as e:
        print("PARSE", f, e); continue
    for s in arr:
        if isinstance(s, dict) and s.get("id") in inp:
            specs[s["id"]] = s

def mins(t):
    h, m = t.strip().split(":")[:2]
    return int(h) * 60 + int(m)
def ranges(v):
    if not v: return []
    out = []
    for part in re.split(r"[,;]", str(v)):
        part = part.strip().replace("–", "-").replace("—", "-")
        m = re.match(r"^(\d{1,2}[:.]\d{2})\s*-\s*(\d{1,2}[:.]\d{2})$", part)
        if m:
            a, b = mins(m.group(1).replace(".", ":")), mins(m.group(2).replace(".", ":"))
            if b <= a: b += 1440
            out.append((a, b))
    return out
def check(s, it):
    errs = []
    dec = s.get("decision")
    if dec not in ("patch", "hide", "no_change"):
        return ["bad decision"]
    if dec != "patch":
        return errs
    rec = s.get("recurrence")
    if rec:
        days = rec.get("days") or []
        if not days or any(d not in range(7) for d in days): errs.append("days")
        st = rec.get("startTime") or ""
        if not re.match(r"^\d{2}:\d{2}:\d{2}$", st): errs.append("startTime fmt")
        dur = rec.get("durationMinutes")
        if not isinstance(dur, int) or not (30 <= dur <= 1439): errs.append(f"duration {dur}")
        sd, ed = rec.get("startDate") or "", rec.get("endDate") or ""
        cur = (it.get("recurrence") or {})
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", sd) or not re.match(r"^\d{4}-\d{2}-\d{2}$", ed): errs.append("date fmt")
        else:
            if sd < TODAY and sd != cur.get("startDate"): errs.append(f"startDate past {sd}")
            if ed < TODAY: errs.append(f"endDate past {ed}")
            if ed > MAXEND: errs.append(f"endDate > {MAXEND}")
            if ed < sd: errs.append("end<start")
            sea = s.get("season") or {}
            if sea.get("basis") in ("official", "copied_2026_pattern") and sea.get("start") and sea.get("end"):
                if sd < sea["start"] and sd >= TODAY and sea["start"] > TODAY: errs.append(f"start {sd} before season {sea['start']}")
                if ed > sea["end"]: errs.append(f"end {ed} after season {sea['end']}")
        hb = s.get("hours_by_day") or {}
        if not isinstance(dur, int) or "fmt" in " ".join(errs):
            pass
        else:
            a = mins(st); b = a + dur
            for d in days:
                rr = ranges(hb.get(str(d)) if isinstance(hb, dict) else None)
                if not rr:
                    errs.append(f"day {d} closed/unknown in hours_by_day"); continue
                if not any(x <= a and b <= y + (1 if y == 1439 else 0) for x, y in rr):
                    errs.append(f"day {d} window {st[:5]}+{dur} outside {hb.get(str(d))}")
    if not isinstance(s.get("isFree"), bool): errs.append("isFree not bool")
    desc = s.get("description")
    if desc:
        L = len(desc)
        if L < 280 or L > 700: errs.append(f"desc len {L}")
        if re.search(r"[<>#*]|\n\s*[-•]", desc): errs.append("desc markup")
    t = s.get("title")
    if t and len(t) > 110: errs.append("title long")
    c = s.get("ctaLink")
    if c and not str(c).startswith("http"): errs.append("cta")
    return errs

apply, problems, hides, nochange = [], [], [], []
missing = [i for i in inp if i not in specs]
for i, it in inp.items():
    s = specs.get(i)
    if not s: continue
    e = check(s, it)
    if e:
        problems.append({"id": i, "place": it["place"], "errs": e, "spec": s, "current_rec": it.get("recurrence")}); continue
    if s["decision"] == "hide": hides.append({"id": i, "place": it["place"], "reason": s.get("hide_reason")}); continue
    if s["decision"] == "no_change": nochange.append(i); continue
    ov = {}
    rec = s.get("recurrence")
    cur = it.get("recurrence") or {}
    if rec:
        newrec = {k: rec[k] for k in ("days", "startTime", "durationMinutes", "startDate", "endDate")}
        newrec["days"] = sorted(set(newrec["days"]))
        if newrec != {**cur, "days": sorted(cur.get("days") or [])}: ov["recurrence"] = newrec
    if s.get("isFree") is not None and s["isFree"] != it.get("isFree"): ov["isFree"] = s["isFree"]
    if s.get("description"): ov["description"] = s["description"].strip()
    if s.get("title"): ov["title"] = s["title"].strip()
    if s.get("ctaLink"): ov["ctaLink"] = s["ctaLink"].strip()
    if ov: apply.append({"id": i, "place": it["place"], "ov": ov})
    else: nochange.append(i)
json.dump(apply, open(AUD + r"\apply.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(problems, open(AUD + r"\problems.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(hides, open(AUD + r"\fix_hides.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"inputs {len(inp)} specs {len(specs)} missing {len(missing)} | apply {len(apply)} hide {len(hides)} nochange {len(nochange)} problems {len(problems)}")
from collections import Counter
print("override fields:", Counter(k for a in apply for k in a["ov"]))
print("problem kinds:", Counter(e.split(" ")[0] for p in problems for e in p["errs"]).most_common(10))
