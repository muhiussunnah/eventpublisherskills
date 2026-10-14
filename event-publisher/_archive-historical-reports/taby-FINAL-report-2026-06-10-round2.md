# Täby Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-10
**Municipality:** Täby (municipalityId: 172600240455582876)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **15** |
| **Events AFTER this session** | **26** |
| **Net new events published this session** | **+11** |
| **Multi-date instances bundled** | **~150+** (Pyssel på torget 19-date + Esplanad konst 7-date + Esplanad låtskrivar 3-date + Rönninge by 24-date weekends + Simhall 40+8-date + Friluftsbad 56-date + Spelmansstämma 1-date + Kanot 1-date) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | taby.se evenemang | **5 events**: Myrans kanotkväll, Pyssel och spel på torget, Esplanad konstprojekt, Esplanad låtskrivarworkshop, Täby spelmansstämma |
| 2 | ronningeby.se + hembygd.se | **1 event**: Rönninge by lantbrukskulturby med ponnyridning |
| 3 | medley.se/taby-simhall + familjebad | **1 event**: Täby simhall familjebad |
| 4 | taby.se badplatser + havochvatten | **1 event**: Sju friluftsbad Skavlöten Ängsholm Hägernäsbadet |

## 8 events published this session

### Mötesplatser och torg (3)
1. **Ung sommar med pyssel och spel på Täby torg från 15 juni till 3 juli** (19-date Mega schack 4-i-rad + bibliotekspyssel)
2. **Esplanad gemensamt konstprojekt skapa bild med poscapennor** (7-date 11-17 juni)
3. **Esplanad låtskrivarworkshop på Täby Kulturhus** (3-date 15-17 juni för ungdomar)

### Sport och uteliv (3)
4. **Myrans kanotkväll med grill vid Hägernäs strand för ungdomar åk 6-9** (17 juni)
5. **Täby simhall familjebad med vattenrutschkanor och småbarnspool** (40+8-date öppen utom 29 juni-7 augusti underhåll)
6. **Sju friluftsbad i Täby med Skavlöten Ängsholm och Hägernäsbadet** (56-date 21 juni-15 augusti)

### Kultur och natur (2)
7. **Rönninge by lantbrukskulturby med bondgårdsdjur kafé och ponnyridning** (24-date lö-sö hela sommaren)
8. **Täby spelmansstämma 2026 med Martin Björklund på Skogberga Spelmansgård** (22 augusti)

### Round 3 deep web search bonus (3)
9. **Loppiskalas i Näsbypark Centrum med utomhus och inomhusloppis** (22 augusti hela centrumet med tusentals saker)
10. **Täby Bakluckeloppis Sveriges största bakluckeloppis fyra dagar** (4-date 15-16 + 22-23 augusti, miljösnäll folkfest fri entré)
11. **Skarpängsleken färgglad lekplats med kemins värld klätterbollar och lång rutschbana** (80-date hela sommaren, gratis utomhuslek)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582876 (not null) | ✅ ALL 11 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 11 |
| Title duplicate check before publish | ✅ ALL 11 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 11 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 11 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 11 |
| Multi-date bundled as single event | ✅ Pyssel 19-date, Esplanad konst 7-date, Esplanad låtskrivar 3-date, Rönninge by 24-date, Simhall 40+8-date, Friluftsbad 56-date |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 11 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 11 |
| Description clean (no JS/code, prose only) | ✅ ALL 11 |
| ctaLink to source page (direct) | ✅ ALL 11 |
| Per Rule #10.6 in-depth + web search | ✅ 7 sources explored (incl Näsbypark loppis + Bakluckeloppis + Skarpängsleken round 3) |

## Skipped (rule-compliant)

- **Anhörigkafé för män + Parkinsons + demens + Navigeringskurs** — vuxen/senior anhörigstöd
- **Musik och gemenskap** — senior
- **Kommunfullmäktige** — politik vuxen
- **Esplanad sommarfest 11 juni** — redan baseline
- **Karby gård onsdagsmusik + Barnens Dag 31 maj** — Barnens Dag redan past
- **Täby Galopp svenskgalopp** — 404 sida
- **Täby Hembygdsförening kalender** — mestadels vuxen-event + Värdsstickardagen
- **Spela badminton och volleyboll** — datum slutar 4 juni (past)
- **Befintliga baseline events** (Babblarna Klonks Klapp-kalas, Visningar Täby kyrka, Friluftsgudstjänst Kullkyrkan, SKU Sommarfestival, Täbydagen, Sommarläsklubben, Susanne Högdahl Holm, Sommarlajv, Midsommarfirande Rönninge by, Esplanad sommarfest, Prisutdelning Täbypris, Bokcirkel, Sagostund från 3 år, Bilderbokscirkel) — redan publicerade

## Coverage assessment

Täby now at **+11 net new (26 total live)**. Täby täcker nu hela ekosystemet med sommarens mötesplatser (Esplanad ungdom + Täby torg pyssel) signaturmål för kulturhistoria (Rönninge by lantbruk + Karby gård) och fullt friluftsutbud (sju friluftsbad + simhall).

Höjdpunkter:
- **Ung sommar Täby torg** — 19 dagar pyssel Mega-spel och bibliotekspyssel hela juni-juli
- **Esplanad ungdomsverkstad** — konstprojekt + låtskrivarworkshop för 13-21 år
- **Myrans kanotkväll** — kanot + grill för åk 6-9 vid Hägernäs strand
- **Rönninge by** — bondgårdsdjur kaffé ponnyridning lö-sö hela sommaren
- **Täby simhall** — familjebad med vattenrutschkanor och småbarnspool (stängd 29 juni-7 aug)
- **Sju friluftsbad** — Skavlöten Ängsholm Hägernäsbadet 21 juni-15 augusti
- **Spelmansstämma 22 augusti** — Martin Björklund från Roslagen på Skogberga

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Täby family-event ecosystem as of 2026-06-10.

Sources:
- [Täby evenemang](https://www.taby.se/arkiv/evenemang)
- [Myrans kanotkväll](https://www.taby.se/arkiv/evenemang/arkiv/2026-06-04-myrans-kanotkvall)
- [Pyssel och spel på torget](https://www.taby.se/arkiv/evenemang/arkiv/2026-05-28-pyssel-och-spel-pa-torget)
- [Esplanad konstprojekt](https://www.taby.se/arkiv/evenemang/arkiv/2026-06-04-esplanad-gemensamt-konstprojekt)
- [Esplanad låtskrivarworkshop](https://www.taby.se/arkiv/evenemang/arkiv/2026-06-01-esplanad-latskrivarworkshop)
- [Täby spelmansstämma](https://www.taby.se/arkiv/evenemang/arkiv/2026-05-28-taby-spelmansstamma-2026-)
- [Rönninge by](https://www.ronningeby.se/)
- [Täby simhall Medley](https://www.medley.se/taby-simhall/bad/familjebad/)
- [Täby badplatser](https://www.taby.se/uppleva-och-gora/natur-och-friluftsliv/badplatser)
- [Loppis Näsbypark Centrum](https://stockholmsmarknader.se/nasbypark/)
- [Täby Bakluckeloppis](https://tabyloppis.com/)
- [Skarpängsleken](https://www.taby.se/uppleva-och-gora/natur-och-friluftsliv/lekplatser/skarpangsleken)
