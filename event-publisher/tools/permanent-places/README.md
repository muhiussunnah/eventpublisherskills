# Permanent places — publishing tools (Värmland + Halland 2026-11-03, Kronoberg + Blekinge 2026-11-10)

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

`choice.json` per place: `{"event": k, "venue": k2, "logo": false, "accept": true, "cta": "…", "rec": {…}, "ev": {…}, "ve": {…}, "og": {…}}`
(image indexes from the contact sheet; `accept` overrides a false-positive check; the dicts override fields).

Getting spec files into the page: **don't use the clipboard while the user works** (their copy overwrote ours on
2026-11-05). Run `compact.py`, print it in ~21 KB chunks and paste each into `javascript_tool` as a template literal
(`__ca[k] = <backtick>…<backtick>`; escape backslash, backtick and `${` first), then compare `__cs()` of every chunk and of
`JSON.stringify(__expand(...))` with the same checksum computed in Python before publishing.
A localhost HTTP server does NOT work: Chrome's Local Network Access check leaves the fetch from
`dashboard.fammap.app` to `127.0.0.1` pending (permission prompt) — stop the server and use chunks.
`MUNIS` and `TODAY` at the top of `build_specs.py` must be set for the new regions; longitude check is 11–24.2.

`audit/` — quarterly accuracy audit of all live places (scan → verification agents → report). See `audit/README.md`.
