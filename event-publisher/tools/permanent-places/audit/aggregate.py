"""Aggregate the verification outputs (out/b_*.json) with the batch inputs → audit_results.json + summary."""
import json, glob, os, collections, re
AUD = r"C:\Users\User\AppData\Local\Temp\claude\793086065a500b32\4ad7473a-f7bd-4184-b47a-6ef00f11c16a\scratchpad\audit"
inp = {}
for f in glob.glob(AUD + r"\batches\b_*.json"):
    for it in json.load(open(f, encoding="utf-8-sig")):
        it["batch"] = os.path.basename(f)[:-5]
        inp[it["id"]] = it
out = {}
bad_files = []
for f in sorted(glob.glob(AUD + r"\out\b_*.json")) + sorted(glob.glob(AUD + r"\out2\r_*.json")):
    try:
        arr = json.load(open(f, encoding="utf-8-sig"))
    except Exception as e:
        bad_files.append((f, str(e))); continue
    for r in arr:
        if isinstance(r, dict) and r.get("id") in inp:
            out[r["id"]] = r
rows = []
for id_, it in inp.items():
    r = out.get(id_)
    c = it["createdAt"]
    era = "researched" if c >= "2026-10-13" else ("oct01" if c >= "2026-10-01" else "aug_sep")
    rows.append({"id": id_, "place": it["place"], "muni": it["muni"], "batch": it["batch"], "createdAt": it["createdAt"],
                 "era": era, "verified": r is not None,
                 "status": (r or {}).get("status"), "action": (r or {}).get("action") or None,
                 "confidence": (r or {}).get("confidence"), "hours_conflict": (r or {}).get("hours_conflict"),
                 "isfree_wrong": (r or {}).get("isfree_wrong"), "desc_wrong": (r or {}).get("desc_wrong"),
                 "official_hours": (r or {}).get("official_hours"), "reopen": (r or {}).get("reopen"),
                 "evidence_url": (r or {}).get("evidence_url"), "evidence_quote": (r or {}).get("evidence_quote"),
                 "note": (r or {}).get("note"), "website": it.get("website"), "cta": it.get("cta"), "rec": it.get("rec"),
                 "isFree": it.get("isFree")})
json.dump(rows, open(AUD + r"\audit_results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def norm_action(a):
    if not a: return "unverified"
    a = a.lower()
    if a == "keep": return "keep"
    if "unpublish" in a: return "unpublish"
    return "fix"
ver = [r for r in rows if r["verified"]]
print("input", len(rows), "verified", len(ver), "bad files", bad_files)
print("\nstatus:", collections.Counter(r["status"] for r in ver).most_common())
print("action (raw):", collections.Counter(r["action"] for r in ver).most_common())
print("action (grouped):", collections.Counter(norm_action(r["action"]) for r in ver).most_common())
for era in ("aug_sep", "oct01", "researched"):
    sub = [r for r in ver if r["era"] == era]
    c = collections.Counter(norm_action(r["action"]) for r in sub)
    print(f"  {era}: n={len(sub)} keep={c['keep']} fix={c['fix']} unpublish={c['unpublish']}")
flags = collections.Counter()
for r in ver:
    a = (r["action"] or "").lower()
    for k in ("fix_hours", "fix_desc", "fix_free"):
        if k in a: flags[k] += 1
print("flags:", dict(flags))
print("\nUNPUBLISH candidates:")
for r in ver:
    if norm_action(r["action"]) == "unpublish":
        print(f"  {r['id']} | {r['place']} | {r['muni']} | {r['status']} | {r['confidence']} | {(r['evidence_quote'] or '')[:90]}")
print("\nCLOSED statuses not marked unpublish:")
for r in ver:
    if r["status"] in ("CLOSED_RENOVATION", "CLOSED_PERMANENT", "MOVED") and norm_action(r["action"]) != "unpublish":
        print(f"  {r['id']} | {r['place']} | {r['status']} | {r['action']} | reopen={r['reopen']}")
