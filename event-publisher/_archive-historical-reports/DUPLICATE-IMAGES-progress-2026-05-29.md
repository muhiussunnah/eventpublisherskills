# Duplicate Images Fix — Progress Update
**Date:** 2026-05-29 (mid-day)
**Cluster being fixed:** 27-event placeholder cluster (Salem/Sigtuna/Solna/Sundbyberg)

## Status: 2 of 27 done

| # | Event | Municipality | Status | New image bytes |
|---|---|---|---|---|
| 1 | Garnudden naturreservat – familjeutflykt vid Bornsjön | Salem | ✅ PATCHED | 205,109 |
| 2 | Skönviksparken Rönninge – familjepark vid sjön | Salem | ✅ PATCHED | 206,716 |
| 3 | Bornsjöns kyrka och fornstig – familjevandring | Salem | ⏳ Prompt sent, ChatGPT stuck | — |
| 4–27 | (24 events) | various | ⏸ Queued in window.__remaining25 | — |

## Working pipeline confirmed

`ChatGPT generates image → fetch bytes in tab 791 → upload to tmpfiles.org (CORS-friendly bridge) → return tmpfiles /dl/ URL → fetch via wsrv.nl proxy from tab 783 → upload to FamMap S3 with campaign.jpg-{ts} filename → PATCH /admin/events/{id} with new images[]`

## Issue encountered

After 2 successful images, ChatGPT image generation for event #3 (Bornsjöns kyrka) stalled — the `<img>` placeholder elements appeared in DOM but the actual image content never loaded (img.naturalWidth stayed at 0 even after 60s+ wait). This is likely:
- ChatGPT rate limiting after rapid back-to-back image generations
- OR session token refresh needed in ChatGPT

## Also fixed during this work

- FamMap JWT token expired mid-session — refreshed by reloading dashboard. Helper code re-installed with fresh `window.__token`.
- localStorage `auth_token` key confirmed for future token refresh.

## Resume instructions (next session)

1. Open dashboard tab `597489783` — verify `window.__token` works by running a test fetch. If expired, reload the dashboard URL.
2. Re-install `window.__patchImg` helper on dashboard tab.
3. Re-create `window.__remaining25` list with prompts (see `DUPLICATE-IMAGES-status-2026-05-29.md`).
4. On ChatGPT tab `597489791`: either continue in current chat OR start a fresh chat. Send prompts one at a time, waiting ~90-120s between each.
5. After each image generates: fetch via tab 791, upload to tmpfiles.org, get `/dl/` URL, run `window.__patchImg(eventId, tmpUrl)` on tab 783.
6. After all 27, re-run hash sweep to verify zero remaining duplicates in cluster 1.

## Remaining 25 event list with prompts

All 25 prompts are pre-written and saved as `window.__remaining25` on dashboard tab (would need to be re-set after any page reload). The list includes:

Bornsjöns kyrka, Lilla Steninge lekpark, ZiggaZing musikföreställning, Nyinvigning Svedenbadet, Sagostund Signalfabriken, Tunadalsbadet, Salems Ridanläggning, Bok+bebis babyboksläsning, Äventyrsgolf Sigtuna, Satutuokio finska sagostund, Steninge slott, Biograf Gröna Ladan, Dansa med bebis, Runstensjakt Sigtuna, Animationer utställning, Sigtuna badplatser, Solna sommargågata, Kick-off lässommar, Sigtuna Bike Arena MTB, Fritidsgården Huset, Bibblan Sommargågatan, Bibblan Hagalunds torg, Huvudsta skatepark, Pop up Ursvik, Sundbyberg Utställning Vad finns.

Each has a hand-written contextual Nordic UGC prompt (5-ingredient formula: subject + Swedish venue + realism details + natural light + "Real life, not staged").
