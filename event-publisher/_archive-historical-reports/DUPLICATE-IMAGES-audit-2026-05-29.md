# Duplicate Image Audit — All 1113 Live Events
**Date:** 2026-05-29
**Triggered by:** Client screenshot showing multiple events sharing the same "library reading group" image

## Method

1. Pulled every live event (1115 total) via `/admin/events?isEnd=false`.
2. Fetched full record for 1113 (2 had no image field).
3. Downloaded each image via wsrv.nl (or directly when host was already wsrv.nl) and computed SHA-256 hash of content bytes.
4. Grouped events by exact byte hash → identified true visual duplicates.

## Top-line numbers

| Metric | Value |
|---|---|
| Total events scanned | 1113 |
| Unique images | 1033 |
| Duplicate groups | 44 |
| Events sharing an image with at least one other event | 121 |
| **Events that need a new unique image** (keep 1 per group, replace n-1) | **77** |

## Root cause (most-affected group: 27 events)

The biggest cluster — **27 events sharing the exact same 106,634-byte image** (hash `4ac362778e0b340d…`) — was created during the Salem, Sigtuna, Solna, Sundbyberg sessions. My publish helper pipeline went:

`ChatGPT-generated image URL → wsrv.nl proxy → upload to FamMap S3`

ChatGPT image URLs expire within ~1 hour. When I queued multiple uploads against the same ChatGPT URL after it had expired, wsrv.nl returned **the same default error placeholder image** for every call. Each upload produced a unique S3 key (because of the `campaign.jpg-{Date.now()}` filename), so my URL-based dedup check passed — but every event ended up with the SAME placeholder image content.

The 27 affected events span Salem (Garnudden, Skönviksparken, Bornsjön kyrka, Tunadalsbadet, Ridanläggning, Fritidsgården), Sigtuna (Lilla Steninge lekpark, Äventyrsgolf, Steninge slott, Biograf Gröna Ladan, Runstensjakt, Bike Arena, badplatser), Solna (ZiggaZing, Svedenbadet, Bok+bebis, Satutuokio, Dansa med bebis, Animationer utställning, sommargågata, Kick-off lässommar, Bibblan x2, Huvudsta skatepark), and Sundbyberg (Sagostund Signalfabriken, Pop up Ursvik, Utställning).

## Full duplicate-group breakdown

| Group | Count | Bytes | Sample | Notes |
|---|---|---|---|---|
| 1 | **27** | 106,634 | Garnudden naturreservat (Salem) | **Placeholder bug** — needs full replacement |
| 2 | 3 | 122,634 | Turinge medeltida kyrka (Nykvarn) | Likely same placeholder bug |
| 3 | 3 | 45,930 | Point_197 onsdagar (Upplands-Bro) | Same venue brand, legit shared poster |
| 4 | 3 | 20,618 | Nationaldagskonsert Vaxholm + 2 UKK | Shared concert series poster |
| 5 | 3 | 20,650 | John Malkovich + Doktor Glas + Bonnie & Clyde (Reginateatern) | DIFFERENT shows sharing image — bug |
| 6 | 3 | 179,004 | Hans Zimmer + RIX FM + Py Bäckman (Uppsala) | DIFFERENT shows sharing image — bug |
| 7 | 3 | 62,226 | Campfire Runö x3 (Österåker) | Same series, legit shared image |
| 8 | 3 | 178,104 | Språkcafé + Helgpyssel + PUNKT (Stockholm) | DIFFERENT events sharing image — bug |
| 9 | 3 | 33,724 | Ungdomszon + Måndaghäng + Sagostund | DIFFERENT events sharing image — bug |
| 10–34 | 2 each | varied | mixed | Mix of legit (vernissage+sista chansen pairs) and bugs |
| 35 | 2 | 28,708 | Nationaldagsfirande Vaxholms kyrka (×2) | **Exact-title duplicate** — accidental |
| 38 | 2 | 9,658 | Manchester United – Atlético de Madrid (×2) | **Exact-title duplicate** — accidental |
| 12 | 2 | 63,392 | IT-hjälp i Sigma Centrum (×2) | **Exact-title duplicate** — accidental |

## Action plan in priority order

1. **HIGH PRIORITY (27 events)**: Group 1 — placeholder bug. All 27 need new unique ChatGPT-generated Nordic UGC images.
2. **MEDIUM PRIORITY (3-event groups idx 5, 6, 8, 9)**: 12 events that are clearly different but share image. Need replacements.
3. **LOW PRIORITY (legit poster shares)**: idx 3, 4, 6, 7, 30–34, 35 — these are vernissage/sista-chansen pairs or same-venue series where shared poster is intentional. Optionally still replace for absolute uniqueness.
4. **TITLE-DUPLICATES (3 events)**: idx 12, 35, 38 — these are accidental duplicate publications, not just shared images. Best fix is to delete one of each pair (per FamMap rules, the user controls deletion).

## Constraints encountered during fix attempt

- Source-site CORS blocks direct og:image fetch from dashboard tab.
- Source sites (salem.se, osteraker.se, etc.) are unreachable from the workspace bash sandbox (proxy 403).
- CORS proxies (corsproxy.io, allorigins.win) also blocked.
- Only viable path for new unique images is **ChatGPT logged-in tab → generate → upload immediately while URL is fresh**.

## Permanent fix going forward (Rule #10.10)

When generating images via ChatGPT for batch publishing:
1. Generate image
2. **Immediately** within 60 seconds, fetch via wsrv.nl proxy, upload to FamMap S3
3. Verify HTTP status 200 AND content-length > 500 bytes (not the wsrv 404 JSON which is ~99 bytes)
4. If verification fails, regenerate and retry — never accept the placeholder
