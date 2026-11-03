# Permanent places — publishing tools (used for Värmland + Halland, 2026-11-03)

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
| `helpers.js` | Paste into the dashboard tab: `__publishPlace(spec)` (dup-title guard → org reuse/create → venue → event, `shouldNotifyUsers:false`, cleans up uploads on failure) and `__queueRun(specs, tag)` (background queue, poll `__bg[tag]`). Needs `window.__muni` (name → municipalityId). |

`choice.json` per place: `{"event": k, "venue": k2, "logo": false, "accept": true, "cta": "…", "rec": {…}, "ev": {…}, "ve": {…}, "og": {…}}`
(image indexes from the contact sheet; `accept` overrides a false-positive check; the dicts override fields).

Getting big spec files into the page without pasting them into a tool call: PowerShell `Clipboard::SetText(file)` →
JS creates a focused `<textarea>` → `ctrl+v` → `JSON.parse(textarea.value)` → restore the user's clipboard.
