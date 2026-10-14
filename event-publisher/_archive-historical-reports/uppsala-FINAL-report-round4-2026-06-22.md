# Uppsala FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-22
**Municipality:** Uppsala (municipalityId: 172600240438805638)

## Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **89** |
| **Live events AFTER** | **110** |
| **Net new events published** | **+21** |
| **Multi-date instances bundled** | ~250 (Sommarklubben 41 + Häng på Lilla torget 35 + Alla Katters 56 + Drop-in Fjällnora 56 + Monster 23 + Höstlovskul 9) |

## Sources processed

| # | Source | Events Published | Notes |
|---|---|---|---|
| 1 | destinationuppsala.se/event-kategori/barn-familj/ (2 pages) | **19 NEW** | 7 dups skipped |
| 2 | uppsala.se/kultur-idrott-fritid/evenemang/ | 0 | All relevant events already published (Sommarlov, Idrottsdag, Hammarskog) |
| 3-8 | ticketmaster/billetto/hejauppsala/upplandsmuseet/bibliotek/facebook/svenskakyrkan | 0 | Aggregate calendars — overlap with already-published events |
| Web search bonus | UKK Häng på Lilla torget | **+1** | 35-date summer hangout event |
| **TOTAL** | | **20 NEW** | (+1 reclassification = +21 live) |

## 20 events published in this session

### Sommarklubben & UKK Sommartorg (3)
1. **Sommarklubben på UKKs sommartorg** — 41 dates (26 juni-23 aug)
2. **Alla Katters café i Pelleparken** — 56 days (22 juni-16 aug)
3. **Block Party Dansa med Jam och Juice** — 8 augusti

### Parksnäckan Concerts (8)
4. **Bamse och Sjörövarskatten** — 11 juli
5. **Medina** — 12 juli
6. **Pappa Kapsyl** — 19 juli
7. **Lilla Spöket Laban** — 26 juli
8. **KAJ (Bara Bada Bastu)** — 9 augusti
9. **Dolly Style** — 16 augusti
10. **Electric Banana Band** — 18 augusti
11. **Tobbe Trollkarl jubileumsshow** — 23 augusti

### Activities & Festivals (5)
12. **Drop-in Äventyrsbana och zipline Fjällnora** — 56 days
13. **Slåtter på Disagården** — 27 juni
14. **Monster och gudar Sommarteater Gottsunda** — 23 dates (25 juli-16 aug)
15. **Historiska dagar i Ulva Kvarn** — 15-16 aug (vendeltid, vikingatid, medeltid)
16. **SciFest 2026 vetenskapsfestival** — 10 oktober (Fyrishov)

### Höst & Vinter events (3)
17. **Höstlovskul Botaniska trädgården** — 9 days (24 okt-1 nov)
18. **Museidagen 2026** — 8 november
19. **Saffransmysteriet LasseMajas** — 12 december (Reginateatern)

### Web search bonus (1)
20. **Häng på Lilla torget** — 35 dates (cornhole, keramik, salsa, musik på UKK Lilla torget)

## Rule compliance verification ✅

| Rule | Result |
|---|---|
| municipalityId not null (Uppsala 172600240438805638) | ✅ ALL 20 |
| Image present for every event (no image = no publish) | ✅ ALL 20 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 20 |
| Title duplicate check before publish | ✅ 7 dups detected and skipped |
| No duplicate images (in-session hash dedup) | ✅ ALL 20 unique source images |
| Only active/upcoming dates (today 2026-06-22+) | ✅ ALL 20 |
| Multi-date bundled (not separate events) | ✅ Sommarklubben 41, Lilla torget 35, Alla Katters 56, Fjällnora 56, Monster 23, Höstlovskul 9 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 20 |
| Description clean (no JS/code, prose only, source-accurate) | ✅ ALL 20 |
| ctaLink to source page | ✅ ALL 20 |
| Web search performed for hidden events | ✅ Found Häng på Lilla torget |

## Skipped (dup with live or out of scope)

- Life. Play. End. — already published (round 2)
- Uppsala Summer Zone 2026 — already published
- Hundens dag — already published as "Hundens dag med Fredrik Steen i Uppsala"
- Pelle Svanslös dag — already published as "Pelle Svanslös dag på UKK"
- Babblarna & Klonks Klapp-kalas — already published
- Allt ljus på Uppsala 2026 — already published
- Djungelboken – The Musical — already published as "Djungelboken – The Musical i Uppsala"
- Sommarlov i Uppsala — already published
- Uppsala idrottsdag — already published
- Lördagar i Hammarskog — already published as "Lördagar i Hammarskog – Naturskolan Uppsala"
- Kulturveckan (intellectual disability focus) — niche audience
- Träffpunkter 65+ — seniors only
- Elitidrott Hylla 2027 — not family

## Coverage assessment

Uppsala live event count: **89 → 110** (+21 net, +24% growth)

Source 1 (destinationuppsala.se barn-familj) fully covered — 26 source events processed, 19 unique published, 7 dups skipped. 
All other 8 sources from spreadsheet checked but content overlapped with already-published events from previous rounds (Round 1-3 had extensive coverage).
Web search bonus added Häng på Lilla torget (UKK summertime hangout).

## Sources

- [destinationuppsala.se barn-familj page 1](https://destinationuppsala.se/event-kategori/barn-familj/)
- [destinationuppsala.se barn-familj page 2](https://destinationuppsala.se/event-kategori/barn-familj/page/2/)
- [uppsala.se evenemang](https://www.uppsala.se/kultur-idrott-fritid/evenemang/)
- [Häng på Lilla torget UKK](https://destinationuppsala.se/event/hang-pa-lilla-torget/)
