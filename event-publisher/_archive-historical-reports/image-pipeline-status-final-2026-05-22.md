# Image Replacement Pipeline — Status & Path Forward
**Date:** 2026-05-22 (final this session)

## Where we landed

### ✅ Proven workflow components
1. **Identification scan** — full 801 events visually scanned, 56 ethnic-mismatch events found
2. **ChatGPT generation** — v4 UGC prompt produces clean Nordic family images (event #4 confirmed)
3. **Image resize** — JS in browser successfully resized 1254×1254 → 500×500 (70KB JPEG)
4. **API endpoints** — POST /admin/image + PATCH /admin/events/{id} both proven from earlier age fixes

### ❌ Blocker hit
**Cross-tab data transfer.** The browser sanitizer blocks:
- Auth tokens (so can't pass fammap JWT to chatgpt tab)
- Data URLs (so can't pass base64 image to my tool result)
- Long encoded strings (treats them as sensitive)

Without one of these, I can't programmatically link "image-in-chatgpt-tab" to "auth-in-fammap-tab" within a single automated flow.

## Recommended path forward (next session)

### Option A: Manual + scripted (FAST, RELIABLE)
Per event:
1. **I generate** the UGC prompt + drive ChatGPT to create the image
2. **You manually** click ChatGPT's download icon → image saves to your Downloads folder
3. **You drag** the file from Downloads to `C:\Users\User\Desktop\eventpublisherskills` folder
4. **I use** `file_upload` tool to put the image into FamMap dashboard's edit-event upload area
5. **I save** the event, triggering FamMap's own upload + image swap

Per event: ~2 min. 56 events × 2 min = ~2 hours.

### Option B: Single-tab approach (more automation)
1. Use only the **dashboard.fammap.app** tab
2. From there, use JS+fetch to retrieve the chatgpt image URL directly (since CDN images allow CORS)
3. Auth token stays on fammap origin, never needs to cross tabs
4. Requires getting the chatgpt URL into fammap tab first — can do via URL hash navigation

This is a one-time setup; once it works, all 56 events can be done in one continuous loop.

### Option C: Server-side (best for scale)
Build a tiny script that:
1. Reads list of 56 events from this scan
2. Calls OpenAI API directly with the UGC prompt
3. Downloads image binary
4. Uploads to FamMap via API
5. PATCHes event

Runs unattended. Could be a Python script.

## All 56 events still needing image replacement
See `bad-images-complete-scan-2026-05-22.md` — full list with event numbers and titles.

## Generated event #4 image (kept on ChatGPT)
ChatGPT conversation: "Image generation request" — Nordic teens at manga club at Swedish library. Image rendered as 1254×1254 PNG, also resized to 500×500 JPEG in browser memory.

## Recommended for next session

**Start with Option B (single-tab approach)** — most automatable, no manual steps per event. I'll implement the hash-based URL transfer and CORS fetch pattern.

If Option B fails due to CORS restrictions, fall back to Option A for the duration of this batch.
