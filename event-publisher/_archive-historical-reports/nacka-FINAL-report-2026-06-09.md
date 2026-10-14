# Nacka Event Publishing — FINAL Report (FULL DEEP DIVE + WEB SEARCH BONUS)
**Date:** 2026-06-09
**Municipality:** Nacka (municipalityId: 172600240455582864)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **22** |
| **Events AFTER this session** | **41** |
| **Net new events published this session** | **+19** |
| **Multi-date instances bundled** | **~200** (Konst i omlopp 15 + Lena Flodman 12 + Hellas 10 + SLTK 15 + SDTK 10 + Saltis IF fotboll 5 + Nacka IBK 15 + Små Grodorna Boo 30 + Små Grodorna Saltsjöbaden 30 + Sång 3 + Turboteater 3 + Animation 3 + others) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | nacka.se/pa-gang-i-nacka (kommun evenemangskalender) | **1 event published**: Utställning Blessings Ann Elfving |
| 2 | nacka.se/sommarlov (sport-och-rörelse + kultur) | Hub for sommarlov - pekar på externa partners |
| 3 | hellassommarlager.se Björknäs IP | **1 event published**: Hellas Sommarläger friidrottsläger V25+V26 |
| 4 | mynewsdesk.com Dieselverkstaden press | **1 event published**: Konst i omlopp sommarutställning (vernissage 13 juni) |
| 5 | nacka.se/kalender-diesel (Dieselverkstaden) | **5 events published**: Sommarkul med lera 8-9 år, Skaparverkstad Måla på canvas, Sång och låtskrivarkurs 11-13 år, Turboteater 11-13 år, Animation 11-13 år fortsättning, Skaparverkstad Midsommar (totalt 6 men Skaparverkstad Midsommar tillkommer) |
| 6 | sltk.se Saltsjöbadens Lawntennisklubb | **1 event published**: Sommarläger junior 3 veckor V24+V25+V26 |
| 7 | sdtk.se Saltsjö-Duvnäs Tennisklubb | **1 event published**: Sommarläger juniorer V25+V26 |
| 8 | nyckelvikensherrgard.se | **1 event published**: Midsommarfirande på Nyckelvikens Herrgård |
| 9 | boofolketshus.se | **1 event published**: Musikschlaget deltävling 10 juni |
| 10 | mynewsdesk.com Lena Flodman press | **1 event published**: Utställning Lena Flodman strandfynd-skulpturer (vår + sommar) |
| 11 | sicklakopkvarter.se/kalendarium | **1 event published**: Sicklaloppet 20 september |
| 12 | nackaif.se Sommarläger | Image proxy DNS-blocked (usercontent.one), skipped despite finding event |
| 13 | sasongsinformation/daglager | Applications closed - skipped |
| 14 | svenskakyrkan Nacka församling Musik | Image too small, skipped Musik och Lyrik series |

## 19 events published this session

### Kommun + bibliotek (1)
1. **Utställning Blessings måleri av Ann Elfving på Nacka Forum bibliotek** (8-14 jun, 7-date bundle)

### Idrottsläger sommar (6)
2. **Hellas Sommarläger 2026 friidrottsläger på Björknäs IP** (V25 + V26, 10-date bundle)
3. **Sommarläger junior 2026 på Saltsjöbadens Lawntennisklubb** (V24 + V25 + V26 grusbanor)
4. **Sommarläger för juniorer V25 och V26 på Saltsjö-Duvnäs Tennisklubb** (Edge Tennis Academy)
5. **Sommarlovscamp 2026 fotbollsträning på Saltsjöbadens IP med Saltsjöbadens IF** (11-17 juni 5-date)
6. **Sommarläger för barn 9-15 år med Nacka IBK innebandy** (V25 + V26 + V32, 15-date bundle)
7. **Sommarsimskola för barn vid Bagarsjöbadet i Saltsjö-Boo med Små Grodorna** (V26-V32, 30-date bundle)

### Sommarsimskola Saltsjöbaden (1)
8. **Sommarsimskola i Saltsjöbaden vid Vårgärdsbadet och Erstaviksbadet med Små Grodorna** (V26-V32, 30-date bundle)

### Dieselverkstaden kultur (6)
9. **Sommarkul med lera 8-9 år sommarlovskurs** (11 juni)
10. **Skaparverkstad Måla på canvas för barn från 5 år** (12 juni)
11. **Sång och låtskrivarkurs 11-13 år sommarlovskurs** (15-17 juni, 3-date)
12. **Turboteater 11-13 år sommarlovskurs** (15-17 juni, 3-date)
13. **Animation 11-13 år fortsättningskurs sommarlovskurs** (15-17 juni, 3-date)
14. **Skaparverkstad Midsommar familjeworkshop** (19 juni drop-in)

### Sommarutställningar (2)
15. **Sommarutställning Konst i omlopp från samling till vardag på Nacka konsthall** (13 jun-6 sep, vernissage 13 juni)
16. **Utställning Lena Flodman skulpturer av strandfynd på Nacka hembygdsmuseum** (vår + sommar, 12-date bundle)

### Folkets hus/musik (1)
17. **Musikschlaget deltävling på Boo Folkets Hus i Nacka** (10 juni 18:00, fri entré)

### Tradition/folkloristisk (1)
18. **Midsommarfirande på Nyckelvikens Herrgård i Nacka** (19 juni - största årliga händelsen)

### Sport/folkfest (1)
19. **Sicklaloppet 2026 löparfest för stora och små i Sickla Köpkvarter** (20 september)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582864 (not null) | ✅ ALL 19 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 19 |
| Title duplicate check before publish | ✅ ALL 19 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 19 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 19 unique hashes |
| Active/upcoming dates only ≥ 2026-06-09 | ✅ ALL 19 |
| Multi-date bundled as single event | ✅ Konst i omlopp 15, Lena Flodman 12, Hellas 10, SLTK 15, SDTK 10, Sång/Turbo/Anim 3-date, Blessings 7 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 19 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 19 |
| Description clean (no JS/code, prose only) | ✅ ALL 19 |
| ctaLink to source page (direct) | ✅ ALL 19 |
| Per Rule #10.6 in-depth + web search | ✅ 14 sources explored |

## Skipped (rule-compliant)

- **Sommarkafée vid Boo Hembygdsförening** — already in baseline
- **Sommarlovskurser på Dieselverkstaden generic** — already in baseline
- **Pingis för seniorer / Trygghetsvandring / Gåfotboll** — senior/vuxen
- **Vem räddar Alfons Åberg sommarteater** — already in baseline
- **Mogendans / Yoga** Boo Folkets Hus — senior/vuxen
- **Spring med ICA Kvantum Runclub** — recurring vuxen löpgrupp
- **Hellas Björknäs som Lidingö-event** — Björknäs IP är Nacka, korrekt publicerat här
- **Nacka IF Sommarläger** — image domain (usercontent.one) DNS-blocked by wsrv proxy, skipped
- **Musik och Lyrik Nacka kyrka serie** — kyrka logo too small (svg)
- **Mini-Muskari Nacka kyrka 12 juni** — kommer behöva bättre bild
- **Konstkalendern + sycle vernissager** — adult-focused
- **Tollare folkhögskola sommarkurser** — vuxen/socionomförberedande
- **Dagläger Velamsund** — applications closed
- **Artipelag** — Värmdö kommun, ej Nacka
- **Past events** — pre 2026-06-09
- **Skansen/Vasa** — Stockholm kommun

## Coverage assessment

Nacka now at **+19 net new (41 total live)**. Nacka has a rich event ecosystem with både kommun-driven (Dieselverkstaden, bibliotek, Nacka konsthall) och externa partners (Hellas Sommarläger, Saltsjöbadens Tennis, SDTK Tennis, Nyckelviken, Sickla Köpkvarter, Saltsjöbadens IF Fotboll, Nacka IBK, Små Grodorna simskolor).

Höjdpunkter:
- **Konst i omlopp** sommarutställning på Nacka konsthall - storkalibrigt verkutbud från Nacka kommuns konstsamling
- **Lena Flodman** parallell utställning på Nacka hembygdsmuseum - Toscana-strandfynd skulpturer
- **6 Dieselverkstaden sommarlovskurser** för 8-13 åringar (lera, canvas, sång, teater, animation, midsommar)
- **3 tennisklubbar** SLTK + SDTK + Hellas friidrott - rikt sommarläger-utbud
- **Midsommar Nyckelviken** - största årliga händelsen i Nacka
- **Sicklaloppet** - signaturlopp för hela familjen
- **Musikschlaget** - inkluderande musikfest för personer med funktionsnedsättningar
- **Saltsjöbadens IF Fotboll** - 5-dagars sommarlovscamp 11-17 juni
- **Nacka IBK innebandy** - 3-vecka sommarcamp för 9-15 åringar
- **Små Grodorna sommarsimskola** - 2 platser (Bagarsjöbadet + Vårgärdsbadet/Erstaviksbadet) genom hela sommaren

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Nacka family-event ecosystem as of 2026-06-09.

Sources:
- [Nacka evenemangskalender](https://www.nacka.se/pa-gang-i-nacka/)
- [Nacka sommarlov](https://www.nacka.se/uppleva--gora/sasongsinformation/sommarlov/)
- [Hellas Sommarläger Björknäs](https://hellassommarlager.se/)
- [Dieselverkstaden evenemang](https://www.nacka.se/valfard-samhallsservice/kulturhusetdieselverkstaden/kalender-diesel/)
- [Konst i omlopp Nacka konsthall](https://www.mynewsdesk.com/se/kulturhuset-dieselverkstaden/pressreleases/aarets-sommarutstaellning-i-nacka-konsthall-och-premiaer-foer-bakfickan-3449844)
- [SLTK Sommarläger 2026](https://sltk.se/sommarlager-2026)
- [Saltsjö-Duvnäs Tennisklubb](https://www.sdtk.se/)
- [Nyckelvikens Herrgård](https://nyckelvikensherrgard.se/nyheter-aktiviteter/)
- [Boo Folkets Hus evenemang](https://www.boofolketshus.se/evenemang/)
- [Lena Flodman Nacka hembygdsmuseum](https://www.mynewsdesk.com/se/kulturhuset-dieselverkstaden/pressreleases/lena-flodman-staeller-ut-paa-nacka-hembygdsmuseum-skulpturer-av-strandfynd-och-parafras-paa-vattentornet-i-jarlaberg-3442321)
- [Sicklaloppet](https://www.sicklakopkvarter.se/kalendarium/sicklaloppet/)
- [Saltsjöbadens IF Sommarlovscamp](https://www.saltsjobadensif.se/fotboll/camper/sommarlovscamper/)
- [Nacka IBK lägerverksamhet](https://nackaibk.se/)
- [Små Grodorna simskola Saltsjö-Boo](https://simskolansmagrodorna.se/nacka/simskola-saltsjo-boo/)
- [Små Grodorna simskola Saltsjöbaden](https://simskolansmagrodorna.se/nacka/simskola-saltsjobaden/)
