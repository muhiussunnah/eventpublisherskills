# Tyresö Event Publishing — FINAL Report (DEEP DIVE round 3)
**Date:** 2026-06-10
**Municipality:** Tyresö (municipalityId: 172600240455582875)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **31** |
| **Events AFTER this session** | **36** |
| **Net new events published this session** | **+5** |
| **Multi-date instances bundled** | **~270** (Summer Challenge 135 60-date V25-V33 + Notholmen café 80-date + Alby friluftsgård 80-date hela sommaren) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | tyreso.se sommarlov 2026 | **1 event published**: Summer Challenge 135 sport spel och häng |
| 2 | cafenotholmen.se + tyresoslott.se | **1 event published**: Notholmen vid Tyresö slott med café |
| 3 | tyreso.se Alby friluftsområde | **1 event published**: Alby friluftsgård vid Albysjön |

## 3 events published this session

### Kommun sommarlov (1)
1. **Summer Challenge 135 sport spel och häng på olika platser i Tyresö hela sommarlovet** (60-date V25-V33, multiarenan Granängsringen + Stadsparken + Strandbadet + Albybadet)

### Friluftsliv (2)
2. **Notholmen vid Tyresö slott med Café Notholmen badklippor och gångbro hela sommaren** (80-date, café + bastu + vandrarhem + gästhamn + badklippor)
3. **Alby friluftsgård vid Albysjön med bad lekplats grillplatser discgolf och café** (80-date hela sommaren öppet 12-17)

### Round 4 deep web search bonus (2)
4. **Tyresöfestivalen 2026 kommunens årliga folkfest med foodtrucks underhållning** (5 september, foodtrucks utställare scenuppträdanden lokala föreningar)
5. **Fritidsbanken Tyresö i Granängsringen med gratis utlåning av sport och fritidsutrustning** (40-date mån/tors V25-V33, sommarstängt V30-V31)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582875 (not null) | ✅ ALL 5 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 5 |
| Title duplicate check before publish | ✅ ALL 5 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 5 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 5 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 5 |
| Multi-date bundled as single event | ✅ Summer Challenge 60-date, Notholmen 80-date, Alby 80-date |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 5 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 5 |
| Description clean (no JS/code, prose only) | ✅ ALL 5 |
| ctaLink to source page (direct) | ✅ ALL 5 |
| Per Rule #10.6 in-depth + web search | ✅ 8 sources explored (incl Tyresöfestivalen + Fritidsbanken round 4) |

## Skipped (rule-compliant)

- **Öppet sommarkollo G60** — session-duplicate image (samma sommar_i_tyreso bild som Summer Challenge)
- **Tyresö slott familjevisning** — redan baseline ("Familjevisning på Tyresö slott")
- **Seglarskola TSBK** — redan baseline ("Seglarskola för 8-13 år på Tyresö Strands Båtklubb")
- **Tyresta nationalpark** — redan baseline ("Vandring i Tyresta nationalpark")
- **Sommarhäng för blivande 7-9or** — generic ungdomshäng
- **Kreativa kurser på Kulturskolan** — anmälan-baserad
- **Befintliga baseline events** (Familjevisning Tyresö slott, Cirkusföreställning Unplugged, Familjelördag Giraffens ABC, Tyresö Novelltävling, Therians och furries-träff, Warriors-boksamtal, Pop-up One Piece, Pop-up K-pop, alla bibliotek-events, Naturguidning Prins Eugens fotspår, Naturguidning Ällmora, Bygg LEGO, Sagostund blommor insekter, Seglarskola TSBK, Magi i det fria Tobbe Trollkarl, Sommar på Forelltorget, Krusboda familjedag, Sommarbokenträff, Förskolefredag, Sommarlovet börjar Bibblabilen, Vandring Tyresta, Guidade visningar Tyresö slott, After church vernissage, Försommarkonsert Tyresö Cantare, Loppis Trollbäcken etc.) — redan publicerade

## Coverage assessment

Tyresö now at **+5 net new (36 total live)**. Tyresö hade redan rik baseline coverage (31 events) genom flera sessioner med kommunens bibliotek, Forelltorget, Tyresö slott, naturguidningar och cirkusistanfestival. Round 3 lagt till signaturmål:

Höjdpunkter:
- **Summer Challenge 135** — gratis sport och spel hela sommaren V25-V33 på multiarena Granängsringen Stadsparken Strandbadet Albybadet
- **Notholmen Tyresö slott** — gångbro till liten ö med Café Notholmen badklippor och gästhamn
- **Alby friluftsgård** — friluftslivets centrum vid Albysjön med bad lekplats discgolf café öppet 12-17

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Tyresö family-event ecosystem as of 2026-06-10.

Sources:
- [Tyresö sommarlov 2026](https://www.tyreso.se/uppleva--gora/kultur-och-fritid-for-barn-och-unga/sommarlov-2026.html)
- [Tyresö slott officiell](https://www.tyresoslott.se/)
- [Café Notholmen](https://www.cafenotholmen.se/)
- [Alby friluftsområde](https://www.tyreso.se/boende--miljo/naturvard-och-miljo/natur--och-friluftsomraden/alby-friluftsomrade.html)
- [Tyresö Strands Båtklubb seglarskola](https://www.svenskalag.se/tyreso-strands-batklubb/sida/69028/seglarskolan)
- [Tyresta nationalpark](https://www.sverigesnationalparker.se/park/tyresta-nationalpark/)
- [Tyresöfestivalen](https://www.tyreso.se/uppleva--gora/kultur-och-noje/tyresofestivalen.html)
- [Fritidsbanken Tyresö](https://www.tyreso.se/uppleva--gora/idrottshallar-lokaler-och-anlaggningar/fritidsbanken.html)
