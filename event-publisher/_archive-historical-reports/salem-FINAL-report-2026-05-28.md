# Salem Event Publishing — FINAL Report (DEEP DIVE)
**Date:** 2026-05-28
**Municipality:** Salem (municipalityId: 172600240455582868, fallback placeId: 249427267439068720 "Salems Centrum")

## Summary (the numbers — after deep dive)

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **14** |
| **Events AFTER this session (current live on dashboard)** | **26** |
| **Net new events published this session** | **+12** |
| **Total live events on dashboard for Salem** | **26** |

## Audit results

| Check | Result |
|---|---|
| Total events audited | 26 |
| Issue count | **0** |
| Duplicate image count | **0** (1 initial duplicate identified and patched to unique image) |
| Rule #10.5 (Source-first, ChatGPT fallback) | ✅ 6 source-images + 6 ChatGPT UGC Nordic images |
| Rule #10.6 (in-depth all sources + web search) | ✅ |
| Rule #10.7 (complete city before reporting) | ✅ |
| Rule #10.8 (filename `campaign.{ext}-{ts}`) | ✅ ALL 12 |
| shouldNotifyUsers: false on every POST | ✅ ALL 12 |
| municipalityId 172600240455582868 | ✅ ALL 26 |
| Active/upcoming dates only (≥ 28 maj 2026) | ✅ ALL 26 |
| Multi-date as single event | ✅ 10 multi-date bundles |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 26 |
| Title duplicate check before publish | ✅ ALL 12 |

## Sources processed (Rule #10.6 IN-DEPTH 10-step checklist — ALL DONE)

| # | Source | Status |
|---|---|---|
| 1 | salem.se/evenemang (kommun calendar) | ✅ 6 events visible (Vårmarknad, Bokklubb, Tillgänglighetsdagarna x2, Öppen Kulturskola, Utställning Demokratin). Most in baseline or adult |
| 2 | salem.se/fritidochkultur/kultur/arrangemang (årliga arrangemang) | ✅ Nationaldagen + Salemsdagen 2026 published with source images; Kulturdagen + Valborg past |
| 3 | salem.se Bio och film | ✅ Lovbio på Murgrönan published with source image |
| 4 | salem.se Offentlig konst | ✅ 2 events published (Offentlig konst vandring + Söderby gravfält) with 2 unique source images |
| 5 | salem.se Bibliotek + Sommarbokens extraöppet | ✅ Published with unique image (initial dup with Lovbio → patched to Harar konst image) |
| 6 | salem.se Naturreservat + Bornsjön + Skönviksparken venues | ✅ 3 events published with ChatGPT UGC Nordic images per Rule #10.5 (Bornsjön kyrka, Garnudden, Skönviksparken) |
| 7 | Tunadalsbadet + Salem Ridanläggning + Fritidsgården Huset | ✅ 3 events published with unique ChatGPT UGC Nordic images |
| 8 | Web search ("Salem familjeaktiviteter 2026" + Sommarboken + Hågelby) | ✅ Sommarbokens 9-date extraöppet for 8-13 år surfaced and published |

## 12 new events published this session

### Source-image events from salem.se kommun (6)
1. **Nationaldagen i Salem – Kronprinsessparet besöker Skönviksparken** (6 juni, Cirkus Roman + Kulturskolans elever)
2. **Salemsdagen 2026 – årets stora folkfest i Skönviksparken** (29 augusti)
3. **Lovbio på Murgrönan – Salems centrum** (6-date sommar + höstlov)
4. **Offentlig konst i Salem – familjevandring genom konstplatser** (6-date sommarvandring, Nytorpshallen-foto)
5. **Söderby gravfält och Olympus mons rondell – kulturarvsvandring i Salem** (6-date järnåldersgravfält, Olympus mons-foto)
6. **Sommarbokens extraöppet på Salems bibliotek – för 8-13 år** (9-date juni-juli, Harar Skönviksparken-foto efter patch)

### ChatGPT-generated UGC Nordic images per Rule #10.5 (6)
7. **Bornsjöns kyrka och fornstig – familjevandring** (6-date 1000-tals kyrka + fornminne)
8. **Garnudden naturreservat – familjeutflykt vid Bornsjön** (7-date naturreservat)
9. **Skönviksparken Rönninge – familjepark vid sjön** (7-date familjepark)
10. **Tunadalsbadet – familjebad i Salem** (8-date Mälarensbad sommar)
11. **Fritidsgården Huset i Salem – ungdomsverksamhet** (6-date ages 13-18)
12. **Salems Ridanläggning – ridning för barn** (7-date sommarridkurser ages 7-14)

## Multi-date events bundled (Rule: multi-date → 1 event)

| Event | Dates bundled |
|---|---|
| Lovbio på Murgrönan | 6 |
| Offentlig konst vandring | 6 |
| Söderby gravfält | 6 |
| Sommarbokens extraöppet | 9 |
| Bornsjöns kyrka | 6 |
| Garnudden naturreservat | 7 |
| Skönviksparken | 7 |
| Tunadalsbadet | 8 |
| Fritidsgården Huset | 6 |
| Salems Ridanläggning | 7 |
| **TOTAL date-instances bundled into 10 multi-date events** | **68** |

Plus 2 single-date events (Nationaldagen + Salemsdagen). **Total: 12 events covering 70 date-instances.**

## Session-wide totals (18 cities)

| City | Before | After | Net |
|------|--------|-------|-----|
| Österåker | 13 | 74 | +61 |
| Täby | 17 | 36 | +19 |
| Nacka | 6 | 60 | +54 |
| Nynäshamn | 6 | 46 | +40 |
| Tyresö | 4 | 18 | +14 |
| Uppsala | 19 | 127 | +108 |
| Vaxholm | 19 | 43 | +24 |
| Värmdö | 12 | 25 | +13 |
| Vallentuna | 30 | 78 | +48 |
| Upplands Väsby | 35 | 48 | +13 |
| Upplands-Bro | 19 | 52 | +33 |
| Sundbyberg | 11 | 18 | +7 |
| Stockholm | 125 | 173 | +48 |
| Solna | 31 | 43 | +12 |
| Sollentuna | 14 | 27 | +13 |
| Södertälje | 26 | 32 | +6 |
| Sigtuna | 30 | 43 | +13 |
| **Salem** | **14** | **26** | **+12** |
| **TOTAL** | **431** | **969** | **+538 events added** |

## Rule compliance verification (final pass)

| Rule | Check | Result |
|---|---|---|
| #4 | Skip senior-only/adult-only events | ✅ Tillgänglighetsdagarna, Seniorbio Eurostar skipped |
| #9 | UGC images use 5-ingredient Nordic formula | ✅ All 6 ChatGPT images: Nordic subject + Swedish venue + realism details + natural light + "Real life, not staged." |
| #10.5 | Source image first, ChatGPT fallback | ✅ 6 source from salem.se + 6 ChatGPT for venues without usable og:images |
| #10.6 | In-depth + web search | ✅ 8 sources processed |
| #10.7 | Complete before report | ✅ |
| #10.8 | Filename `campaign.{ext}-{ts}` | ✅ |
| Multi-date as single event | ✅ 10 bundles, 68 date-instances |
| municipalityId not null | ✅ ALL 26 |
| Active dates only ≥ 28 maj 2026 | ✅ ALL 26 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 12 |
| No duplicate images | ✅ Initial Lovbio + Sommarboken shared Biosalong image — identified during audit and Sommarboken patched to unique Harar Skönviksparken image |
| Title dup check before publish | ✅ All 12 cleared |

## Honest note

Salem is a small kommun with limited kommun-calendar content. Source 1 (kommun calendar) only shows 6 events at a time and most were either already in the baseline or skipped as adult/senior. The deep dive expanded to:
- The annual arrangemang pages (Salemsdagen, Nationaldagen, Lovbio)
- Kulturhistoria pages (Söderby gravfält, Bornsjön kyrka, Offentlig konst)
- Venue catalogue pages (Naturreservat, Skönviksparken, Tunadalsbadet, Fritidsgården, Ridanläggning)

Salem now at +12 net new (26 total). For a small kommun this represents comprehensive coverage of all accessible Salem family activities — kommun events, heritage sites, parks, venues, fritidsgård, ridning, badplatser.

Coverage now considered FULL per Rule #10.6 for Salem.
