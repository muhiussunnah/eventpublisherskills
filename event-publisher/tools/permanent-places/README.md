# Permanent places — publishing tools (Värmland + Halland 2026-11-03, Kronoberg + Blekinge 2026-11-10, last 5 regions 2026-11-18)

The scratchpad is wiped between sessions, so the working tools live here. Each Python script has a `PP = '…/scratchpad/pp/'`
path at the top: point it at the current session's scratchpad folder before running. Run Python as `python -I -X utf8`.

| File | What it does |
|---|---|
| `extract.py <html> <out.json>` | Pulls `const EMBEDDED = {places:[…]}` out of the client HTML, prints region/kommun counts, writes the selected regions (edit the region tuple). |
| `brief_pp.md` | Research brief for the subagents (one group of ~8 places each → `res_<G>.json`). |
| `show.py <G…>` | One-screen summary per place (org, venue, hours, recurrence, flags) for review. |
| `imgprep.py <G…>` | Downloads every candidate image as a 1080 square (wsrv) + logos, writes contact sheets `sheet_<G>_<n>.jpg` to look at. |
| `chaindup.py "<glob>"` | dHash check of candidate images against existing chain-event images in the app (`chain_urls.txt`). ≤10 = duplicate. |
| `build_specs.py <G…>` | Rule checks (desc 300–650, title "Plats – …", 2 interests, window open on every listed day, no personal email/mobile, coords) and builds publish specs from `res_*.json` + `choice.json`. |
| `compact.py <specs.json> <out.json>` | Shrinks specs (~45 %) for the JS-literal transfer: raw image URLs instead of wsrv URLs, hours as `DHHMMHHMM`, days as a digit string, venue description dropped (= event description). |
| `transfer_audit.js` | Paste after `helpers.js`: `__expand(compact)` + `__cs(text)` checksum, `__auditPublished(specs, done)` field-by-field re-read, `__buildEventsTSV()` rows for the sheet's Events tab. |
| `helpers.js` | Paste into the dashboard tab: `__publishPlace(spec)` (dup-title guard → org reuse/create → venue → event, `shouldNotifyUsers:false`, cleans up uploads on failure) and `__queueRun(specs, tag)` (background queue, poll `__bg[tag]`). Needs `window.__muni` (name → municipalityId). |

| `groups.py <pp/>` | Splits `sel.json` into research groups of ~8 places (`group_<G>.json`, `groups_index.json`), biggest kommuner first; edit `EXIST` (items already in the app) and the region order. |
| `review.py <G…>` | Compact one-block-per-place review of `res_<G>.json` (org, venue, hours, recurrence, flags, note) and default entries in `choice.json`; warns when a group's result misses or adds items. |
| `setc.py '<json>'` | Merges decisions into `choice.json` (`{"277": {"event": 1, "venue": 2}, "308": {"skip": "reason"}}`). |
| `cs.py <file…>` | Length + checksum of a spec file (same formula as `__cs` in the page) and an ASCII check. |
| `page_tools.js` | Paste after `helpers.js`: file-upload transfer (`__prep`), dHash duplicate-photo check against every published live event (`__buildRef`, `__dupCheck2`), `__chainAfter`, `__saveIds`, `__auditPublished`, `__localSpecs`. |
| `localimg.py <G> <i…>` | For places whose images the proxy cannot fetch: downloads the originals with a browser UA, writes 1080 crops + a 512 logo to `local/` and `local_<i>.json` with `local:<file>` image names (see `__localSpecs`). |
| `outcome.py [ids.json]` | Outcome of every place of the run (published with window/period/ID, skipped with reason, already in the app) → `outcome.json` + counts per region. |
| `mkreport.py <out.md> <head.md> <tail.md>` | Final report: per-region table, published table, skipped table, seasonCopied and short-span follow-ups around hand-written head/tail. |

`choice.json` per place: `{"event": k, "venue": k2, "logo": false, "logoDark": true, "accept": true, "skip": "reason", "hold": "reason", "crop": "&a=top", "cta": "…", "rec": {…}, "ev": {…}, "ve": {…}, "og": {…}}`
(image indexes from the contact sheet; `accept` overrides a false-positive check; the dicts override fields).

Getting spec files into the page (**preferred since 2026-11-18, costs no tokens and no clipboard**): create
`<input type="file" id="__specfile" multiple>` in the dashboard page, find its ref, send `batchN.json` with the browser
`file_upload` tool, then `await __prep('batchN.json', <len>, <checksum>)` (numbers from `cs.py`). `logoDark` puts a white
logo on the app's dark blue instead of white; `hold` keeps a place out of the batch (e.g. until local images are ready);
`og: {"reuseId": "<organizationId>"}` forces an existing organizer, `og: {"email": null}` works around the unique e-mail.
Rebuild the batch after the LAST decision (a place accepted after the build is silently missing).

Older way of getting spec files into the page: **don't use the clipboard while the user works** (their copy overwrote ours on
2026-11-05). Run `compact.py`, print it in ~21 KB chunks and paste each into `javascript_tool` as a template literal
(`__ca[k] = <backtick>…<backtick>`; escape backslash, backtick and `${` first), then compare `__cs()` of every chunk and of
`JSON.stringify(__expand(...))` with the same checksum computed in Python before publishing.
A localhost HTTP server does NOT work: Chrome's Local Network Access check leaves the fetch from
`dashboard.fammap.app` to `127.0.0.1` pending (permission prompt) — stop the server and use chunks.
`MUNIS` and `TODAY` at the top of `build_specs.py` must be set for the new regions; longitude check is 11–24.2.

`audit/` — quarterly accuracy audit of all live places (scan → verification agents → report). See `audit/README.md`.
