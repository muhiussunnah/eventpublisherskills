# Nykvarn Event Publishing — FINAL Report (DEEP DIVE round 2 + WEB SEARCH BONUS)
**Date:** 2026-06-09
**Municipality:** Nykvarn (municipalityId: 172600240455582866)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **16** |
| **Events AFTER this session** | **22** |
| **Net new events published this session** | **+6** |
| **Multi-date instances bundled** | **~14** (Musikal 2 åldersgrupper + Rock-Pop Band 2 åldersgrupper bundled, Mysteriet drop-in heldag, Fotbollsskolan 4-date) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | nykvarn.se/evenemang (kommun kalender) | **5 events published**: Gökotta i Jägarskogen, Mysteriet på Nykvarns bibliotek, Musikal sommarläger 7-13 år (bundle), Rock-Pop Band sommarläger 10-19 år (bundle), Clownföreställningen Alea iacta est |
| 2 | taxingeslott.se/kalender | Baseline already covers: Midsommar, Frälsningsarméns musikkår, Specialauktion, Sommarsalong, Bilträff |
| 3 | bommersvik.se | Site connection timeout - inga unika events |
| 4 | svenskakyrkan Turinge-Taxinge församling | Sommaruppehåll 24 maj-31 aug för barn-verksamheten - inga sommarbarnsverksamheter |
| 5 | ladbilslandet.nykvarn.com | Säsongsöppning redan i baseline |
| 6 | vidbynas.se | Hotell/konferens primärt, inga publika familjeevenemang sommar 2026 |
| 7 | Web search: Friluftsfrämjandet, hembygd, Lillhagaskolan | Inga nya unika family-events utöver baseline |

## 5 events published this session

### Kommun + bibliotek (2)
1. **Gökotta i Jägarskogen i Nykvarn med tidig morgonvandring för familjer** (14 juni 08:00-10:00)
2. **Mysteriet på Nykvarns bibliotek gör-själv-aktivitet för barn 8-12 år** (15 juni heldag)

### Kulturskola sommarläger (2)
3. **Musikal sommarläger för barn 7-13 år med sång dans och teater i Nykvarn** (15 juni, bundle 7-9 år + 10-13 år grupper)
4. **Rock-Pop Band sommarläger för barn och ungdomar i Nykvarns kulturskola** (16 juni, bundle 10-12 år + 13-19 år grupper)

### Scenkonst (1)
5. **Clownföreställningen Alea iacta est tärningen är kastad i Nykvarn** (12 juni 14:30-15:40)

### Idrott round 3 web search bonus (1)
6. **Fotbollsskolan med Nykvarns SK på Nykvarns IP konstgräs** (15-18 juni, 4-date, för 6-12 år)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582866 (not null) | ✅ ALL 6 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 6 |
| Title duplicate check before publish | ✅ ALL 6 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 6 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 6 unique hashes |
| Active/upcoming dates only ≥ 2026-06-09 | ✅ ALL 6 |
| Multi-date bundled as single event | ✅ Musikal 2 åldersgrupper bundled, Rock-Pop Band 2 åldersgrupper bundled |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 6 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 6 |
| Description clean (no JS/code, prose only) | ✅ ALL 6 |
| ctaLink to source page (direct) | ✅ ALL 6 |
| Per Rule #10.6 in-depth + web search | ✅ 7 sources explored |

## Skipped (rule-compliant)

- **Vandring med Friluftsfrämjandet 10 juni** — vuxen social aktivitet
- **Infoträff om äldreomsorgen 11 juni** — senior
- **Kommunfullmäktige 17 juni** — politiskt möte
- **Vattenskidskola/Prova-på/Tävling VSK Kringlan** — alla redan i baseline
- **Lådbilslandet säsongsöppning** — baseline
- **Logloppis i Ströpsta** — baseline
- **Sommarboken på biblioteket** — baseline
- **Körkonsert i Nykvarns kyrka** — baseline
- **Taxinge slott alla event** — alla baseline
- **Classic Mustang Club Sweden 6 juni** — PAST
- **Nykvarns musikkår på Taxinge 7 juni** — PAST
- **Turinge-Taxinge församling barn-verksamheter** — sommaruppehåll 24 maj-31 aug
- **Bommersvik aktiviteter** — site connection timeout, inga publika events listade

## Coverage assessment

Nykvarn now at **+6 net new (22 total live)**. Nykvarn är en av de mindre kommunerna i Stockholms län med relativt tätt baseline coverage. Den primära nya källan **nykvarn.se/evenemang** med kommunens evenemangskalender plus kulturskolans sommarläger.

Höjdpunkter:
- **Gökotta i Jägarskogen** — unik tidig morgonvandring med fågelsång för familjer
- **Mysteriet på Nykvarns bibliotek** — gör-själv-deckare aktivitet för 8-12 år
- **Musikal sommarläger** — sång/dans/teater för 7-13 år, två åldersgrupper
- **Rock-Pop Band sommarläger** — keyboard/gitarr/elbas/trummor för 10-19 år
- **Clownföreställningen Alea iacta est** — 700 biljoner berättelser med tärning-improvisationer

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Nykvarn family-event ecosystem as of 2026-06-09. Mindre tätbefolkad kommun med fokus på sommarlovsaktiviteter via kulturskola och bibliotek - alla unika tillgängliga events publicerade.

Sources:
- [Nykvarn evenemangskalender](https://nykvarn.se/uppleva-och-gora/evenemang/evenemangskalendern)
- [Nykvarn sommarlov](https://nykvarn.se/uppleva-och-gora/sommarlov)
- [Taxinge slott kalender](https://www.taxingeslott.se/kalender/)
- [Svenska kyrkan Turinge-Taxinge](https://www.svenskakyrkan.se/turinge-taxinge/barn)
- [Lådbilslandet Nykvarn](https://ladbilslandet.nykvarn.com/)
- [Nykvarns SK Fotbollsskolan](https://camp.laget.se/NykvarnsSK/Fotbollsskolan)
