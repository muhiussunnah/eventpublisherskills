# App Image Diagnosis — Why agent-published events show broken images in famies app
**Date:** 2026-08-30
**Status:** ✅ OPTION A DONE — 107/113 re-hosted to S3 & app-verified. 6 remain (dead source, all past events).

## FIX RESULT (Option A executed 2026-08-30)

- Re-hosted **107 of 113** app-broken images to fammap S3 via POST /admin/image + PATCH images[].
  - 104 upload.wikimedia.org + 3 commons.wikimedia.org → all now `fammap-storage.s3…/campaign/…webp`.
- Full re-scan of all 4230 events afterward: **wikimediaLeft = 0**. ✅
- App-client (okhttp UA) curl re-test of Liseberg, Universeum, World of Volvo, Malmö Opera, Malmö
  Reptilcenter → all **200 image/webp** (were 403 before). User's exact complaint resolved.
- **6 NOT fixed** = all "Cirkus Brazil Jack" events sharing one dead source (braziljack.se/CBJ-2025.jpg
  now returns HTML, not image; also bot-blocks okhttp with 455). ALL 6 are **PAST events**
  (last dates 2026-06-24 … 07-08, today 08-30) → they violate Rule F (upcoming-only) anyway.
  Recommendation: delete them (past) or leave (won't surface in upcoming feed). Left as-is pending
  user call — no wrong image forced on them.
- Building-only / wrong-place pictures (Gripsholm-for-Christinehof, Laos-pool-for-Österlenbadet, etc.)
  were preserved as-is per user instruction ("Option A first, quality/building images pore solve korbo").
  These are the deferred Round-B backlog.

## The complaint

Dashboard (dashboard.fammap.app/events) shows images fine for Göteborg events (Liseberg, Universeum,
Göteborgs naturhistoriska museum, Sjöfartsmuseet Akvariet, World of Volvo) and Skåne round events,
but the famies mobile app shows black/broken image boxes for exactly those events. Manually created
events (Bohus fästning, Trollhättans Bowlinghall, Kanalmuseet, Saab Car Museum…) show fine everywhere.

## ROOT CAUSE (proven)

Recent publishing rounds (Göteborg + Skåne) **hotlinked external image URLs directly into `images[]`**
instead of uploading to fammap S3 via `POST /admin/image`. Mostly **Wikimedia** URLs.

**Wikimedia returns 403 Forbidden to any HTTP client without a browser User-Agent.**

Proof (curl, 2026-08-30):

| URL | okhttp/4.9.2 (Android app client) | Chrome UA |
|---|---|---|
| upload.wikimedia.org (Volvo, Malmö Opera…) | **403** text/plain | 200 image/jpeg |
| commons.wikimedia.org/wiki/Special:FilePath (Liseberg, Universeum) | **403** | 200 (redirect→image) |
| fammap-storage.s3.eu-north-1.amazonaws.com (manual events) | 200 image/webp | 200 |
| images.unsplash.com | 200 | 200 |
| wsrv.nl, naturkartan-cdn, biblioteket.stockholm.se, tyreso.se, upplands-bro.se, sundbyberg.se, ticketm.net, wixstatic | 200 | 200 |
| braziljack.se | **455** (bot block) | — |

- Dashboard = browser → Wikimedia serves the image → looks fine to admin.
- famies app = okhttp (React Native image loader) → Wikimedia 403 → broken black box.
- This also explains "manual events work": the dashboard UI upload flow always lands files in fammap S3.

## Database audit (full scan of all 4230 events via GET /admin/events?limit=100&page=N)

Image host of `images[0]` across ALL events:

| Host | Count | App status |
|---|---|---|
| fammap-storage.s3.eu-north-1.amazonaws.com | 2909 | ✅ works |
| wsrv.nl (proxy → mostly cdn.pixabay.com 413, kommun sites) | 520 | ✅ loads via proxy, BUT fragile; ~1/5 sampled = 404 (source gone) |
| images.unsplash.com | 513 | ✅ loads (but forbidden by image rules, brittle) |
| **upload.wikimedia.org** | **104** | ❌ 403 in app |
| **commons.wikimedia.org** (Special:FilePath redirect) | **3** | ❌ 403 in app |
| uploads.naturkartan-cdn.se | 72 | ✅ loads |
| biblioteket.stockholm.se | 21 | ✅ loads |
| www.upplands-bro.se 14, tyreso 7, sundbyberg 6, barnistan 4, prismic 3, ticketm 2, misc 1s | ~50 | ✅ mostly load |
| **braziljack.se** | **6** | ❌ 455 in app |
| INVALID (malformed value) | 35 | ❌ broken everywhere (era 3424, biblioteket round) |
| NONE/empty | — | (see scan) |

**App-broken total: 113 events** (107 wikimedia + 6 braziljack) + 35 INVALID + unknown # of dead wsrv sources.

### Recent-era split (eventId first 4 digits ≈ creation round)

| Era | Round | Total | S3 ✅ | wikimedia ❌ | other-ext |
|---|---|---|---|---|---|
| 4358 | Göteborg venues | 16 | 13 | 3 (Liseberg, Universeum, Naturhistoriska — commons Special:FilePath) | 0 |
| 4359 | Göteborg | 26 | 0 | 22 | 4 (lillabommen, gokartcentralen, jumpyard, cms.leosplay) |
| 4360 | Skåne 33 cities | 126 | 44 | **82** | 0 |

→ matches user report exactly: "Skåne 126 er maximum show korche na" = 82/126 broken.

## Secondary finding — some wikimedia picks are factually WRONG images

- "Christinehof slott" → image is **Gripsholm castle** (Mariefred, wrong place)
- "Österlenbadet" → image is a **luxury resort pool in Luang Prabang, Laos**
- Building-only exteriors violate image-rules ("families/kids engaging" standard) anyway.

So a plain re-host would preserve wrong/rule-violating pictures for some events.

## Fix recipe (when approved)

Rebuild the list fresh from the dashboard tab (page context, localStorage.auth_token):

```javascript
// 1. scan all pages (43 x limit=100) -> window.__ALL
// 2. bad = images[0] host includes 'wikimedia' or 'braziljack.se'
// 3. per event:
//    a. fetch source image (works from browser UA), draw to 500x500 canvas -> jpeg blob
//    b. POST https://api.fammap.app/admin/image  (multipart 'file',
//       filename MUST be `campaign.jpg-${Date.now()}` — Rule #10.8)
//    c. GET /admin/events/{id} -> spread full body, override images:[s3Url]
//    d. PATCH /admin/events/{id}  (full body required: placeId,title,description,images,
//       lat,lng,address,isFree,parentMinAge,parentMaxAge,childMinAge,childMaxAge,ctaLink,ctaText,dates)
```

Option A (quick, ~15-20 min): re-host the SAME images to S3 → app renders, but keeps wrong-place +
rule-violating pictures.
Option B (rule-compliant, ~2h due to ChatGPT ~10 img/4 min rate limit): regenerate all 113 via
ChatGPT per image-rules (Nordic families/kids engaging), upload to S3, PATCH.
Hybrid: A now for correct-subject images, B for wrong/generic ones.

## Hardening backlog (separate rounds, not urgent)

1. 513 unsplash + ~150 venue-site/CDN hotlinks + 520 wsrv → re-host to S3 (source alive, straight copy).
2. 35 INVALID (era 3424) + dead wsrv sources (~20%?) → need fresh images.
3. **NEW PERMANENT RULE for skill:** `images[]` must ONLY ever contain
   `https://fammap-storage.s3.eu-north-1.amazonaws.com/...` URLs. NEVER store an external URL,
   whatever the host — the app's okhttp client gets UA-blocked (wikimedia 403, braziljack 455),
   proxies/temp hosts rot, and the dashboard browser hides the breakage from the admin.
   Verify after every publish: `images[0].startsWith('https://fammap-storage')`.

## API notes learned this session

- `GET /admin/events?limit=100&page=N` — list works (max limit ≤ ~100–500; 500 fails, 100 ok).
  `search`/`offset`/`perPage` params → 400 "/query must NOT have additional properties".
  Response: `{data: {events: [{eventId, title, images, isFree, status, isRecurring, ...}], totalEvents}}`.
- Content filter blocks tool outputs containing URLs with query strings — strip to origin+pathname
  when returning URLs from javascript_tool.
