# Accuracy audit of all live permanent places

Used on 2026-11-05 (report `../../../PERMANENT-PLACES-ACCURACY-AUDIT-2026-11-05.md`). Set `AUD` at the top of each
script to the session's scratchpad `audit/` folder; run Python as `python -I -X utf8`.

| File | What it does |
|---|---|
| `scan.py` | Reads `det.json` (all recurring events with venue data), fetches each website/ctaLink and greps closure phrases → `scan.json`. |
| `brief_verify.md` | Brief for the verification agents (one batch of ~28 places → `out/b_NN.json`). |
| `aggregate.py` | Joins `batches/` inputs with `out/` + `out2/` (retry) outputs → `audit_results.json`, prints counts per batch era. |
| `report.py` | Builds the markdown report (sections A–J) from `audit_results.json` + `venue_issues.json`; scrubs phones/e-mails/names. |

The full method is in `references/technical-patterns.md` → "Accuracy audit of all live permanent places".
