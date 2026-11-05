"""Build the markdown audit report from audit_results.json (+ venue_issues.json)."""
import json, collections, re
AUD = r"C:\Users\User\AppData\Local\Temp\claude\793086065a500b32\4ad7473a-f7bd-4184-b47a-6ef00f11c16a\scratchpad\audit"
rows = json.load(open(AUD + r"\audit_results.json", encoding="utf-8"))
vi = json.load(open(AUD + r"\venue_issues.json", encoding="utf-8"))
OUT = r"F:\eventpublisherskills\eventpublisherskills\event-publisher\PERMANENT-PLACES-ACCURACY-AUDIT-2026-11-05.md"

def grp(a):
    if not a: return "unverified"
    a = a.lower()
    if a == "keep": return "keep"
    if "unpublish" in a: return "unpublish"
    return "fix"
PHONE = re.compile(r"(?<![\w\-:/.])(?:\+46|0)[\d\s\-]{6,14}\d(?![\w\-])")
MAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
TEXT_COLS = {"Evidence", "Why", "Official season / hours", "Official hours", "Official", "What is wrong", "What was tried", "Reopens"}
def _phone(m):
    d = re.sub(r"\D", "", m.group(0))
    return "[tel]" if 8 <= len(d) <= 12 else m.group(0)
def esc(s, scrub=False):
    s = (s or "").replace("|", "/").replace("\n", " ").strip()
    if scrub:
        s = MAIL.sub("[e-post]", s)
        s = PHONE.sub(_phone, s)
        s = re.sub(r"(?i)\b(ring|kontakta|contact|call)\s+[A-ZÅÄÖ][a-zåäöé]+", r"\1 [namn]", s)
    return s
def rec_txt(r):
    rec = r.get("rec") or {}
    d = rec.get("days") or []
    names = "Sun Mon Tue Wed Thu Fri Sat".split()
    ds = "daily" if len(d) == 7 else ",".join(names[x] for x in sorted(d))
    st = (rec.get("startTime") or "")[:5]
    dur = rec.get("durationMinutes") or 0
    try:
        h, m = int(st[:2]), int(st[3:5]); e = h * 60 + m + dur
        et = f"{(e // 60) % 24:02d}:{e % 60:02d}"
    except Exception:
        et = "?"
    return f"{ds} {st}–{et}, {rec.get('startDate')}→{rec.get('endDate')}"

ver = [r for r in rows if r["verified"]]
unv = [r for r in rows if not r["verified"]]
c_all = collections.Counter(grp(r["action"]) for r in ver)
flags = collections.Counter()
for r in ver:
    a = (r["action"] or "").lower()
    for k in ("fix_hours", "fix_desc", "fix_free"):
        if k in a: flags[k] += 1
status = collections.Counter(r["status"] for r in ver)
closed_now = [r for r in ver if r["status"] in ("CLOSED_RENOVATION", "CLOSED_PERMANENT", "MOVED") and grp(r["action"]) != "keep"]
season_closed = [r for r in ver if r["status"] == "SEASON_ONLY" and grp(r["action"]) != "keep"]
unpub = [r for r in ver if grp(r["action"]) == "unpublish"]
nvp = [r for r in ver if r["status"] == "NOT_A_VISITOR_PLACE"]
unclear = [r for r in ver if r["status"] == "UNCLEAR"]

L = []
L.append("# Permanent places — accuracy audit of every live recurring place (2026-11-05)\n")
L.append("**Trigger:** Örebro läns museum e-mailed that the app shows wrong information about them (building closed for "
         "renovation since 2018, reopens late 2027; the app said \"Öppet tisdag till söndag\"). The CEO asked how many "
         "other permanent places are wrong.\n")
L.append("**Method:** all live recurring events (`isRecurring`, `/admin/events?isEnd=false`) were pulled with their venue "
         "data (1,365). 1) Automated scan of every website for closure phrases + HTTP status. 2) 56 verification agents "
         "(about 25–28 places each) checked every place against its official website / kommun page: status, opening hours and "
         "season vs the published recurrence, description claims, price (isFree). 3) Separate checks for duplicates and "
         "events attached to the wrong venue. Nothing was edited in the app during the audit.\n")
L.append("## Headline numbers\n")
L.append("| | Count |\n|---|---|")
L.append(f"| Live recurring places audited | {len(rows)} |")
L.append(f"| Verified against an official source | {len(ver)} |")
L.append(f"| Correct as published (keep) | {c_all['keep']} |")
L.append(f"| Needs a correction (hours / season / description / price) | {c_all['fix']} |")
L.append(f"| Should be unpublished (closed, moved, booking-only, unverifiable) | {c_all['unpublish']} |")
L.append(f"| Not verified (agent output missing) | {len(unv)} |")
L.append(f"| &nbsp;&nbsp;— wrong opening hours or season | {flags['fix_hours']} |")
L.append(f"| &nbsp;&nbsp;— wrong description | {flags['fix_desc']} |")
L.append(f"| &nbsp;&nbsp;— wrong isFree flag | {flags['fix_free']} |")
L.append(f"| Closed right now (renovation / permanently / moved) but shown as open | {len(closed_now)} |")
L.append(f"| Seasonal places published as open all year (closed now) | {len(season_closed)} |")
L.append(f"| Not a drop-in visitor place (booking-only, ticketed venue) | {len(nvp)} |")
L.append(f"| Duplicate recurring events of the same place | {sum(len(v) for v in vi['duplicates'].values() if isinstance(v, list))} events in {len([k for k in vi['duplicates'] if not k.startswith('_')])} groups |")
L.append(f"| Events attached to another place's venue (wrong address/pin) | {len([k for k in vi['wrong_venue'] if not k.startswith('_')])} |")
L.append("")
L.append("### By publishing batch\n")
L.append("| Batch | Verified | Keep | Fix | Unpublish | Keep % |\n|---|---|---|---|---|---|")
for era, label in (("aug_sep", "Aug–Sep 2026 (template hours, no per-place check)"), ("oct01", "1 Oct 2026 (Jönköping region batch, before the per-place process)"), ("researched", "13 Oct–3 Nov 2026 (Gävleborg, Södermanland, Värmland, Halland — researched per place)")):
    sub = [r for r in ver if r["era"] == era]
    c = collections.Counter(grp(r["action"]) for r in sub)
    pct = round(100 * c["keep"] / len(sub)) if sub else 0
    L.append(f"| {label} | {len(sub)} | {c['keep']} | {c['fix']} | {c['unpublish']} | {pct}% |")
L.append("")
L.append("Status distribution: " + ", ".join(f"{k} {v}" for k, v in status.most_common()) + "\n")
L.append("Note: \"wrong hours\" is strict — it includes cases where the published window overruns the official "
         "closing time by 30–60 minutes, as well as places published daily that are closed several days a week.\n")

def table(title, items, cols):
    L.append(f"## {title} ({len(items)})\n")
    L.append("| " + " | ".join(h for h, _ in cols) + " |")
    L.append("|" + "---|" * len(cols))
    for r in items:
        L.append("| " + " | ".join(esc(str(f(r)), h in TEXT_COLS) for h, f in cols) + " |")
    L.append("")

table("A. Closed now but shown as open — unpublish or cut the dates", closed_now, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("Status", lambda r: r["status"]), ("Reopens", lambda r: r["reopen"]), ("Published", rec_txt),
    ("Evidence", lambda r: (r["evidence_quote"] or "")[:140]), ("Source", lambda r: r["evidence_url"]),
    ("Conf.", lambda r: r["confidence"])])
table("B. Recommended unpublish (closed / moved / booking-only / cannot be verified)", unpub, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("Status", lambda r: r["status"]), ("Why", lambda r: ((r["evidence_quote"] or "")[:120] + " " + (r["note"] or "")[:80])),
    ("Conf.", lambda r: r["confidence"])])
table("C. Seasonal places published as open all year (closed at the moment)", season_closed, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("Published", rec_txt), ("Official season / hours", lambda r: (r["official_hours"] or "")[:140]),
    ("Reopens", lambda r: r["reopen"]), ("Action", lambda r: r["action"]), ("Conf.", lambda r: r["confidence"])])
fix_hours = [r for r in ver if "fix_hours" in (r["action"] or "").lower() and r["status"] not in ("SEASON_ONLY",) and grp(r["action"]) != "unpublish"]
table("D. Open places with wrong hours (published window outside official hours)", fix_hours, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("Published", rec_txt), ("Official hours", lambda r: (r["official_hours"] or "")[:150]),
    ("Action", lambda r: r["action"]), ("Conf.", lambda r: r["confidence"])])
fix_free = [r for r in ver if "fix_free" in (r["action"] or "").lower()]
table("E. Wrong isFree flag", fix_free, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("App says free", lambda r: r["isFree"]), ("Official", lambda r: ((r["evidence_quote"] or "")[:100] + " " + (r["note"] or "")[:60])),
    ("Conf.", lambda r: r["confidence"])])
fix_desc = [r for r in ver if "fix_desc" in (r["action"] or "").lower()]
table("F. Wrong description text", fix_desc, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("What is wrong", lambda r: (r["desc_wrong"] or r["note"] or "")[:200]), ("Conf.", lambda r: r["confidence"])])
L.append("## G. Events attached to the wrong venue (address and map pin belong to another place)\n")
L.append("| Event ID | Problem |\n|---|---|")
for k, v in vi["wrong_venue"].items():
    if not k.startswith("_"): L.append(f"| {k} | {esc(v, True)} |")
L.append("\n## H. Venue named after an organisation / kommun instead of the place\n")
L.append("| Event ID | Problem |\n|---|---|")
for k, v in vi["venue_named_after_operator_or_kommun"].items():
    if not k.startswith("_"): L.append(f"| {k} | {esc(v, True)} |")
L.append("\n## I. Duplicates (same place published more than once)\n")
L.append("| Place | Event IDs |\n|---|---|")
for k, v in vi["duplicates"].items():
    if not k.startswith("_"): L.append(f"| {k} | {', '.join(v)} |")
L.append("\nAgents also reported duplicate pairs inside their batches (Odenbadet, Åsle Tå, Reijmyre, Torvalla simhall, Ösmo simhall, "
         "Hållö fyr, Vilanbadet, Tomteland, Marionetteatern, Laserdome Surbrunnsgatan/Vasastan, Racehall, Yoump Kungens Kurva, "
         "DVVJ, Sea4fun, Falkängen, Gullmarsborg, Lek & Bus Nacka, Bouldering Stockholm, Ragnerud, Strömma); see the per-place notes.\n")
table("J. Could not be verified (UNCLEAR) — manual check needed", unclear, [
    ("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"]),
    ("What was tried", lambda r: ((r["evidence_quote"] or "")[:100] + " " + (r["note"] or "")[:100])), ("Action", lambda r: r["action"])])
if unv:
    table("K. Not verified (no agent output)", unv, [("Place", lambda r: r["place"]), ("Kommun", lambda r: r["muni"]), ("Event ID", lambda r: r["id"])])
L.append("## Root cause\n")
L.append("- The Aug–Sep 2026 batch (~1,130 places) was created from template values: 504 events carry exactly `daily 10:00–16:00 "
         "to 2027-12-31`, 179 `daily 10:00–18:00`; 455 are marked free although many are paid venues. Opening status, season, "
         "hours and price were not checked against the official source per place.\n"
         "- The 1 Oct 2026 batch (Jönköping region, 57) used real hours more often but still copied weekday windows onto "
         "weekends and missed seasonal closures.\n"
         "- The 13 Oct–3 Nov batches (Gävleborg, Södermanland, Värmland+Halland) were researched per place from official "
         "sources; their remaining issues are small (a season end date one day off, isFree left false on free outdoor "
         "places, two booking-only farms that should not be drop-in places).\n"
         "- Also found: website fields that now point to casino spam (Solna simhall, Tolvåkerbadet, Långe Erik, "
         "hantverkfalkangen.se, steningeslott.com) and dead domains; these links must be replaced.\n")
L.append("## Remediation plan\n")
L.append("1. Unpublish (reversible, venue `isPublished:false` or move to a `[Dold]` holding venue) every place in A and B.\n"
         "2. Cut `endDate` / set the 2027 `startDate` for every seasonal place in C.\n"
         "3. Re-set recurrence from the official hours for D, set `isFree` for E, rewrite descriptions for F.\n"
         "4. Re-point G to their own venues (create the venue at the real address), rename H, unpublish the extra copies in I.\n"
         "5. Manual check of J, then keep or unpublish.\n"
         "6. New rule: no permanent place goes live without an official source for status + hours + price, and every live "
         "place is re-verified each quarter (`tools/permanent-places/` has the scan + verification brief).\n")
open(OUT, "w", encoding="utf-8").write("\n".join(L))
print("written", OUT, "lines", len(L))
print("verified", len(ver), "keep", c_all["keep"], "fix", c_all["fix"], "unpublish", c_all["unpublish"], "unverified", len(unv))
print("closed_now", len(closed_now), "season_closed", len(season_closed), "nvp", len(nvp), "unclear", len(unclear), flags)
