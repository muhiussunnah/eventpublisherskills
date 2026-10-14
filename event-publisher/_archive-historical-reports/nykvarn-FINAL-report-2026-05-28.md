# Nykvarn Event Publishing — FINAL Report (DEEP DIVE)
**Date:** 2026-05-28
**Municipality:** Nykvarn (municipalityId: 172600240455582866, fallback placeId: 340017316232201359 "Nykvarn general venue")

## Summary (the numbers)

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **16** |
| **Events AFTER this session (current live on dashboard)** | **26** |
| **Net new events published this session** | **+10** |
| **Total live events on dashboard for Nykvarn** | **26** |

## Audit results

| Check | Result |
|---|---|
| Total events audited | 26 |
| Issue count | **0** |
| Duplicate image count | **0** |
| Rule #10.5 (Source-first, ChatGPT fallback) | ✅ 7 source-images + 3 ChatGPT UGC Nordic images |
| Rule #10.6 (in-depth all sources + web search) | ✅ |
| Rule #10.7 (complete city before reporting) | ✅ |
| Rule #10.8 (filename `campaign.{ext}-{ts}`) | ✅ ALL 10 |
| shouldNotifyUsers: false on every POST | ✅ ALL 10 |
| municipalityId 172600240455582866 | ✅ ALL 26 |
| Active/upcoming dates only (≥ 28 maj 2026) | ✅ ALL 26 |
| Multi-date as single event | ✅ 3 multi-date bundles |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 26 |
| Title duplicate check before publish | ✅ ALL 10 |

## Sources processed (Rule #10.6 IN-DEPTH 10-step checklist — ALL DONE)

| # | Source | Status |
|---|---|---|
| 1 | nykvarn.se/uppleva-och-gora/evenemang/evenemangskalendern | ✅ 13 events scanned. 2 new family events published with source og:images (Modellflygets dag MFD, Vandring med Friluftsfrämjandet Bommersvik). Rest in baseline or adult (Må bra fika, Medborgardialog, Infoträff äldreomsorgen, INSTÄLLT Kommunpolisen) |
| 2 | taxingeslott.se (slottets egna kalender) | ✅ 5 family events published with source images (Mustang Club, Frälsningsarméns musikkår, Midsommarfirande, Bilträff, Nykvarns musikkår med Åsa Dellham) |
| 3 | VSK Kringlan vattenskidklubb | ✅ Vattenskidskola + Prova-på-dag + Vattenskidtävling already in existing baseline. New ChatGPT-image event added (Sundsviks badplats Lilla Turingen) |
| 4 | Yngern naturreservat | ✅ ChatGPT UGC family fiske/vandring event published |
| 5 | Turinge medeltida kyrka + Turinge-Taxinge Hembygdsförening | ✅ ChatGPT UGC kulturarvsutflykt published |
| 6 | Vidbynäs Gård + Bommersvik | ✅ Vidbynäs Brasserie (Mors Dag) in baseline. Bommersvik covered via Friluftsfrämjandet vandring |
| 7 | Lådbilslandet i Nykvarn | ✅ Already in baseline (Säsongsöppning 2026) |
| 8 | Web search ("Nykvarn familjeaktiviteter 2026") | ✅ Confirmed all major Nykvarn family venues covered |

## 10 new events published this session

### Source-image events (7)
1. **Modellflygets dag MFD på Påldalen** (30 maj, Södertälje Modellflygklubb)
2. **Vandring med Friluftsfrämjandet – Bommersvik** (9 juni)
3. **Classic Mustang Club Sweden besöker Taxinge slott** (6 juni)
4. **Frälsningsarméns musikkår – konsert på Taxinge slott** (14 juni)
5. **Midsommarfirande på Taxinge slott 2026** (19 juni, Assar Åberg dragspel)
6. **Bilträff på Taxinge slott – oktober 2026** (11 oktober)
7. **Nykvarns musikkår med Åsa Dellham – konsert på Taxinge slott** (7 juni)

### ChatGPT-generated UGC Nordic images per Rule #10.5 (3)
8. **Yngern naturreservat – familjefiske och vandring** (7-date sommarsäsong)
9. **Sundsviks badplats Lilla Turingen – familjebad i Nykvarn** (9-date sommarsäsong)
10. **Turinge medeltida kyrka och Turinge-Taxinge Hembygdsförening** (6-date sommarvisning)

## Multi-date events bundled (Rule: multi-date → 1 event)

| Event | Dates bundled |
|---|---|
| Yngern naturreservat | 7 |
| Sundsviks badplats | 9 |
| Turinge kyrka | 6 |
| **TOTAL date-instances bundled into 3 multi-date events** | **22** |

Plus 7 single-date events. **Total: 10 events covering 29 date-instances.**

## Session-wide totals (19 cities)

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
| Salem | 14 | 26 | +12 |
| **Nykvarn** | **16** | **26** | **+10** |
| **TOTAL** | **447** | **995** | **+548 events added** |

## Rule compliance verification (final pass)

| Rule | Check | Result |
|---|---|---|
| #4 | Skip senior-only/adult-only events | ✅ Må bra fika, Medborgardialog, Infoträff äldreomsorgen, Konstkollo vuxna skipped |
| #9 | UGC images use 5-ingredient Nordic formula | ✅ All 3 ChatGPT images: Nordic subject + Swedish venue + realism details + natural light + "Real life, not staged." |
| #10.5 | Source image first, ChatGPT fallback | ✅ 7 source (nykvarn.se + taxingeslott.se) + 3 unique ChatGPT for venues without og:images |
| #10.6 | In-depth + web search | ✅ 8 sources processed |
| #10.7 | Complete before report | ✅ |
| #10.8 | Filename `campaign.{ext}-{ts}` | ✅ |
| Multi-date as single event | ✅ 3 bundles, 22 date-instances |
| municipalityId not null | ✅ ALL 26 |
| Active dates only ≥ 28 maj 2026 | ✅ ALL 26 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 10 |
| No duplicate images | ✅ Each event uses unique image (7 unique source + 3 unique ChatGPT UGC) |
| Title dup check before publish | ✅ All 10 cleared |

Coverage now considered FULL per Rule #10.6 for Nykvarn's accessible family events and venues.
