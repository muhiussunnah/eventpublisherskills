# Duplicate Images Fix — Status & Handoff
**Date:** 2026-05-29
**Status:** Audit complete (1113 events scanned). Fix STARTED but BLOCKED on ChatGPT mode.

## What's done this turn

1. **Full visual-dedup scan** across all 1113 live events (downloaded + SHA-256 hashed every image).
2. **Root cause identified**: 27-event cluster sharing same 106,634-byte placeholder image — caused by ChatGPT URL expiry during Salem/Sigtuna/Solna/Sundbyberg batch publishing. wsrv.nl returned same error placeholder for every expired URL → same content uploaded to S3 with different keys.
3. **77 events** identified needing new unique images across 44 duplicate groups.
4. **Audit report written**: `DUPLICATE-IMAGES-audit-2026-05-29.md`
5. **Publish helper installed** on dashboard tab — `window.__patchImg(eventId, imgUrl)` ready.
6. **27-event list saved** to `window.__cluster27` on dashboard tab.

## What's blocked

ChatGPT defaulted to **"Instant" mode** when I sent the first image-generation prompt — Instant mode is text-only, no image generation. The chat created ("Photo Request Garnudden Reserve") but only returned a feedback question, not an image.

## Resume instructions for next session

1. Tab `597489791` is open at ChatGPT. **Switch the model from "Instant" to GPT-4o or GPT-image-1** in the ChatGPT model picker (top-left dropdown).
2. Dashboard tab `597489783` has `window.__token`, `window.__patchImg(id, imgUrl)`, `window.__cluster27`, `window.__visualDups2`, and `window.__toReplace` all live.
3. For each of the 27 events in `window.__cluster27`:
   - Prompt ChatGPT for unique Nordic UGC photo matching the event (use the 5-ingredient formula: Nordic subject + Swedish venue + realism details + natural light + "Real life, not staged.")
   - Wait for image URL from `files.oaiusercontent.com`
   - On dashboard tab: `await window.__patchImg(eventId, chatgptUrl)`
   - Verify `{ok: true}` and `size > 5000` in result
4. After all 27, re-run the hash sweep to confirm zero duplicates remain for that cluster.
5. Then proceed to remaining 50 events in smaller clusters (`window.__toReplace.slice(27)`).

## Full duplicate-group reference

See `DUPLICATE-IMAGES-audit-2026-05-29.md` for the complete 44-group breakdown including:
- Group 1: 27 events (Salem/Sigtuna/Solna/Sundbyberg) — placeholder bug, must replace ALL
- Group 2: 3 Nykvarn events (Turinge, Sundsvik, Yngern) — placeholder bug, must replace all
- Groups 3-9: 3-event clusters mixed (some legit shared posters, some bugs)
- Groups 10-43: 2-event clusters (mix of legit vernissage+sista-chansen pairs and bugs)
- Groups 12 (IT-hjälp ×2), 35 (Nationaldagsfirande Vaxholm ×2), 38 (Manchester United ×2) — exact-title duplicate events

## Permanent rule fix (added to memory)

**Rule #10.10** — After uploading any ChatGPT-generated image via wsrv.nl pipeline, **verify** the resulting S3 object is > 5000 bytes AND not the known 106,634-byte placeholder hash (`4ac362778e0b340d…`). If it is, regenerate ChatGPT image immediately and retry — never publish the placeholder.
