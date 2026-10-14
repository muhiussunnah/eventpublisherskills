# Botkyrka Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-08
**Municipality:** Botkyrka (municipalityId: 172600240447194249)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **36** |
| **Events AFTER this session** | **53** |
| **Net new events published this session** | **+17** |
| **Multi-date instances bundled** | **~145** (Sommar i konstverkstan 25 + Rumble in the Jungle 20 + Ateljé BK 20 + Pappersmakeri 20 + Klapphage 14 + Cirkus Cirkör sommarlovskurs 15 + Folk Lab Verkstaden 20 + others) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | botkyrka.se evenemangsarkiv (310 events) | Mostly recurring/baseline. 4 unique published: Sommarlov i Hågelbyparken, Utställning Från spargris till Swish, Folk Lab Verkstaden, Tumba bruksmuseum |
| 2 | botkyrka.se/uppleva-och-gora/botkyrkas-stora-sommarguide | Linked back to evenemangsarkiv |
| 3 | hagelby.se kalender | **5 family-friendly events published**: This is Botkyrka festival, Barnteater Gräs, Bakluckeloppis 3-date bundle, Klapphage 14-date bundle, Barnteater sommar 6-date bundle, Ekorrstigen upptäckarstig |
| 4 | cirkor.se / subtopia.se | **4 events published**: Sommarlovskurs cirkus 15-date bundle, Sommarlovskurs Dans 5-date Subtopia, Skulpturworkshop 2-date, Therian-mask-workshop |
| 5 | botkyrkakonsthall.se | **3 events published**: Sommar i konstverkstan 25-date bundle, Ateljé BK 20-date bundle Thursdays, Rumble in the Jungle utställning 20-date bundle |
| 6 | tumbabruksmuseum.se | **1 event** Pappersmakeri 20-date Thu-Sun bundle |
| 7 | svenskakyrkan.se/botkyrka/konserter | 404 — URL not accessible. Web search suggested ut sommarkonserter exist but no direct kalender |
| 8 | ticketmaster.se/city/botkyrka | No city-specific filter, generic Sweden page returned |

## 17 events published this session

### Hågelbyparken (4) — kommun events
1. **Sommarlov i Hågelbyparken med roliga aktiviteter** (12 juni - 17 aug long-running)
2. **This is Botkyrka familjefestival i Hågelbyparken** (27 juni)
3. **Barnteater Gräs familjeföreställning** (24 juni)
4. **Bakluckeloppis i Hågelbyparken sommar 2026** (3-date bundle: 28 jun, 26 jul, 30 aug)

### Hågelbyparken (3) — hagelby.se direct
5. **Klapphage på Hågelby 4H-gård – klappa fåren** (14-date bundle tisdag/fredag jun-aug)
6. **Barnteater sommar 2026 i Hågelbyparken** (6-date bundle juli-aug)
7. **Ekorrstigen upptäckarstig för barn** (long-running)

### Cirkus Cirkör / Subtopia (4)
8. **Sommarlovskurs i cirkus för barn 7-14 år på Cirkus Cirkör Alby** (15-date 3 weeks: 14-18 jun, 22-26 jun, 10-14 aug)
9. **Sommarlovskurs Dans för 10-14 åringar på Subtopia** (5-date 22-26 jun)
10. **Skulpturworkshop för unga på Subtopia i Alby** (2-date 2-3 juli)
11. **Therian-mask-workshop på Subtopia i Alby** (9 juli)

### Botkyrka konsthall (3)
12. **Sommar i konstverkstan på Botkyrka konsthall** (25-date bundle tisdag-fredag 16 jun - 14 aug)
13. **Ateljé BK konstverkstad för unga på Botkyrka konsthall** (20-date Thursday recurring)
14. **Eric Magassa Rumble in the Jungle utställning** (20-date bundle Tue-Sat 18 apr - 3 okt)

### Bibliotek/utställning (2)
15. **Utställning Från spargris till Swish på Tumba bruksmuseum** (long-running hela 2026)
16. **Tillverka eget handpapper på Tumba bruksmuseum – sommar** (20-date Thu-Sun bundle 14:00)

### Hallunda (1)
17. **Folk Lab Verkstaden digital kreativitet i Hallunda Folkets Hus** (20-date Thursday recurring 17-21)

## Multi-date bundles

| Event | Dates bundled |
|---|---|
| Sommar i konstverkstan | 25 |
| Rumble in the Jungle | 20 |
| Ateljé BK | 20 |
| Pappersmakeri | 20 |
| Folk Lab Verkstaden | 20 |
| Cirkus Cirkör sommarlovskurs | 15 |
| Klapphage | 14 |
| Barnteater sommar | 6 |
| Sommarlovskurs Dans Subtopia | 5 |
| Bakluckeloppis | 3 |
| Skulpturworkshop, Ansgar etc | 2 |
| **TOTAL date-instances bundled** | **~150** |

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240447194249 (not null) | ✅ ALL 17 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 17 |
| Title duplicate check before publish | ✅ ALL 17 cleared (with substring + fuzzy match in helper) |
| Source images (Rule #10.5) — unique per event | ✅ ALL 17 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 17 unique hashes |
| Active/upcoming dates only ≥ 2026-06-08 | ✅ ALL 17 |
| Multi-date bundled as single event | ✅ 11 multi-date bundles (150 instances) |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 17 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 17 |
| Description clean (no JS/code, prose only) | ✅ ALL 17 |
| ctaLink to source page (direct) | ✅ ALL 17 |
| Per Rule #10.6 in-depth + web search | ✅ 8 sources + multiple bonus venues explored |

## Skipped (rule-compliant)

- **Folk Lab Odling på orten** — only kommun logo as og:image, no usable unique image
- **Folk Lab Entreprenörskap** — same generic logo issue
- **Appoteket på Tumba bibliotek** — senior-targeted + only logo image
- **Zumba Fitness/Guld** (recurring kategorier) — vuxen-fitness
- **Sammanträden, Mötesplats för funktionsnedsättningar, God hälsa för seniorer** — adult/senior business
- **Nationaldagen 6 juni** — PAST (today 8 juni)
- **Askungen, Drakar & Dragqueens, Folk Lab Odling, Invigning Rösträtt** — alla PAST
- **Author samtal på uzbekiska, etc** — niche adult cultural
- **Cirkus Cirkör shows in baseline** (Blåsväder, Marklyft, Vem var min pappa, Tanter på rymmen, 20 Years Later) — already in baseline
- **Ticketmaster Botkyrka** — no city-specific filter
- **Svenska kyrkan Botkyrka kalender** — 404 page
- **Subtopia Cirkus residens, Korpen Zumba** — recurring vuxen-fokus
- **Mat i mörker (Subtopia related)** — vuxen

## Coverage assessment

Botkyrka now at **+17 net new (53 total live)**. All 8 spreadsheet sources plus 4 bonus venues (Hågelbyparken direct, Cirkus Cirkör / Subtopia ecosystem, Botkyrka konsthall, Tumba bruksmuseum) thoroughly explored. Major attractions covered:

- **Hågelbyparken folkpark** — major summer family destination with 4H-gård, barnteater, klapphage, Ekorrstigen, festival
- **Cirkus Cirkör + Subtopia kreativa kluster i Alby** — 4 unique events including Sommarlovskurs, Dans, Skulptur, Therian
- **Botkyrka konsthall i Fittja** — 3 high-value events including sommarkonstverkstan and 6-månaders utställning
- **Tumba bruksmuseum** — 2 unique events including 100-årig Lyckoslanten utställning
- **Hallunda Folkets Hus Folk Lab** — 1 digital kreativitet workshop

Coverage now considered **FULL** per Rule #10.6 for accessible Botkyrka family-event ecosystem as of 2026-06-08.

Sources:
- [Botkyrka evenemangsarkiv](https://www.botkyrka.se/evenemangsarkiv)
- [Botkyrkas stora sommarguide](https://www.botkyrka.se/uppleva-och-gora/botkyrkas-stora-sommarguide)
- [Hågelbyparken kalender](https://hagelby.se/kalender/)
- [Cirkus Cirkör Alby holiday courses](https://www.cirkor.se/en/courses/holiday-courses-alby/)
- [Subtopia kalendarium](https://subtopia.se/kalendarium/)
- [Botkyrka konsthall](https://www.botkyrkakonsthall.se/)
- [Tumba bruksmuseum barn och familj](https://tumbabruksmuseum.se/besok/barn-och-familj/)
