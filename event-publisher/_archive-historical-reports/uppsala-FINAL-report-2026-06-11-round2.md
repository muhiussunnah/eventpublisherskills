# Uppsala Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-11
**Municipality:** Uppsala (municipalityId: 172600240438805638)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **87** |
| **Events AFTER this session** | **100** |
| **Net new events published this session** | **+13** |
| **Multi-date instances bundled** | **~530** (Linnéträdgården 95-date + Botaniska 24-date weekend + Domkyrkan 12-date söndag + Takvandring slott 38-date weekend + Hågadalen 110-date + Linnés Hammarby 70-date + Bror Hjorths Hus 70-date + Parksnäckan 70-date + Biotopia 110-date + Gustavianum 80-date) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | uu.se Linnéträdgården + destinationuppsala | **1 event**: Linnéträdgården sommaröppet med guidning |
| 2 | uu.se Botaniska trädgården | **1 event**: Botaniska trädgården Tropiska växthuset orangeri |
| 3 | svenskakyrkan.se uppsaladomkyrka + destinationuppsala | **1 event**: Uppsala domkyrka söndagsvisning |
| 4 | destinationuppsala.se Takvandring | **1 event**: Takvandring på Uppsala slott |
| 5 | uppsala.se + naturkartan Hågadalen | **1 event**: Hågadalen-Nåstens naturreservat |
| 6 | destinationuppsala.se Linnés Hammarby | **1 event**: Linnés Hammarby 1700-talsgård |
| 7 | brorhjorthshus.se | **1 event**: Sommarutställning Primus Mortimer Pettersson |
| 8 | parksnackan.se | **1 event**: Parksnäckan sommarprogram med Lilla spöket Laban |
| 9 | biotopia.nu | **1 event**: Biotopia biologiskt museum Vasaparken |
| 10 | uu.se Gustavianum | **1 event**: Gustavianum med Bruno Liljefors-utställning |
| 11 | destinationuppsala.se + uppsala.se Ulva kvarn | **1 event**: Ulva kvarn hantverksby med Ulvabadet |
| 12 | regionuppsala.se Wiks slott | **1 event**: Wiks slott guidning med kojbyggarland |
| 13 | destinationuppsala.se Lövstabruk | **1 event**: Lövstabruk med Barnens Bruk och Cahman-orgeln |

## 13 events published this session

### Trädgårdar och natur (3)
1. **Linnéträdgården sommaröppet med daglig guidad visning av Carl von Linnés trädgård i centrala Uppsala** (95-date, 1300 arter sexualsystem skattjakt 11-17)
2. **Botaniska trädgården med Tropiska växthuset orangeri och guidade visningar varje helg i Uppsala** (24-date helger, Café Victoria barockträdgård)
3. **Hågadalen-Nåstens naturreservat med Kung Björns hög Fjärilsstigen och Linnés vandringsleder** (110-date)

### Slott och historia (2)
4. **Takvandring på Uppsala slott med fantastisk utsikt över stan lördag och söndag hela sommaren** (38-date 30 maj - 18 okt)
5. **Linnés Hammarby unik 1700-talsgård med världens största levande Linneansk växtsamling** (70-date 23 juni - 31 aug)

### Religiösa och kulturmonument (1)
6. **Guidad visning av Uppsala domkyrka Nordens största katedral varje söndag klockan 12.30** (12-date söndagar)

### Museer (3)
7. **Sommarutställning på Bror Hjorths Hus med Primus Mortimer Petterssons färgstarka bildvärld** (70-date 11 juni - 23 aug, familjeverkstäder 5 juli + 2 aug)
8. **Biotopia interaktivt biologiskt museum i Vasaparken med dioramor av Upplands djur och natur** (110-date)
9. **Gustavianum sommaröppet med Bruno Liljefors-utställning och Anatomiska teatern dagliga guidningar** (80-date 12 juni - 13 sep, dagliga guidningar 24 juni - 1 sep)

### Scen och evenemang (1)
10. **Parksnäckan i Stadsträdgården sommarkonserter och familjeföreställningar inklusive Lilla spöket Laban** (70-date juni-aug, Cleo Petra Marklund Lilla spöket Laban 26 juli Electric Banana Band)

### Round 3 deep web search bonus (3)
11. **Ulva kvarn hantverksby norr om Uppsala med glasblåseri silversmide café restaurang och Ulvabadet** (95-date 12 juni - 13 september, hantverkare från 1759 + Blåsippsbackens glass + tillgänglighet)
12. **Guidning på Wiks slott vid Mälaren med kojbyggarland och sommarcafé fredag lördag söndag i juli och augusti** (12-date 24 juli - 16 aug, medeltidsslott + Wikparken kojbyggarland + sommarcafé Lilla matsalen)
13. **Lövstabruk vallonbruksort med Barnens Bruk lekmiljö av Sven Nordqvist Cahman-orgel och historisk herrgård** (95-date, en av världens främsta järnbruk + Cahman-orgeln 1728 + Barnens Bruk av Pettson-skaparen Nordqvist)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240438805638 (not null) | ✅ ALL 13 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 13 |
| Title duplicate check before publish | ✅ ALL 13 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 13 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 13 unique hashes |
| Active/upcoming dates only ≥ 2026-06-11 | ✅ ALL 13 |
| Multi-date bundled as single event | ✅ Linnéträdgården 95, Botaniska 24, Domkyrkan 12, Takvandring 38, Hågadalen 110, Hammarby 70, Bror Hjorth 70, Parksnäckan 70, Biotopia 110, Gustavianum 80 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 13 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 13 |
| Description clean (no JS/code, prose only) | ✅ ALL 13 |
| ctaLink to source page (direct) | ✅ ALL 13 |
| Per Rule #10.6 in-depth + web search | ✅ 13 sources explored (incl Ulva kvarn + Wiks slott + Lövstabruk round 3) |

## Skipped (rule-compliant)

- **Linnés trädgårdsfest 23 maj** — past
- **Skärgårdsbåtens dag** — past
- **Befintliga baseline events** (87 events inkl UKK-konserter Babblarna Klonks Klapp-kalas Familjekonsert Peter och vargen Pelle Svanslös Dag RIX FM Festival Valfestivalen Hogwarts Magic Symphony Hundens dag Hammarskog Lekutställning Lill-Disa Disagården Midsommarafton Disagården Sommarlov i Uppsala Kulturnatten Uppsala Allt ljus på Uppsala Familjespåret UPP-täckaren Arkeologidagen Uppsala Summer Zone Bakluckeloppis Ulva kvarn Memento Mori Life Play End Elsa Beskow Reginateatern-föreställningar Bibliotek-program) — redan publicerade

## Coverage assessment

Uppsala now at **+13 net new (100 total live)**. Uppsala hade redan extremt rik baseline coverage (87 events) genom UKK Reginateatern Upplandsmuseet Gamla Uppsala museum Disagården bibliotek och kommunens sommarprogram. Round 2 + 3 lagt till signaturmål från Linné-arvet universitetsmuseerna och kringliggande herrgårdar/bruk:

Höjdpunkter:
- **Linnéträdgården** — Carl von Linnés ursprungliga trädgård med 1300 arter och daglig guidning
- **Botaniska trädgården** — barockträdgård + Tropiska växthuset med Uppsalas enda regnskog
- **Linnés Hammarby** — 1700-talsgård med världens största levande Linneansk växtsamling
- **Uppsala domkyrka** — Nordens största katedral med Gustav Vasa och Linné begravda
- **Uppsala slott takvandring** — vandra på slottets tak med säkerhetsutrustning och utsikt
- **Hågadalen-Nåsten** — Kung Björns hög bronsåldersgrav och Linnés vandringsleder
- **Bror Hjorths Hus** — studiomuseum med Primus Mortimer Pettersson-utställning
- **Biotopia** — 100-årigt interaktivt biologiskt museum i Vasaparken med Upplands dioramor
- **Gustavianum** — Anatomiska teatern + Bruno Liljefors-donation + Augsburgska konstskåpet
- **Parksnäckan** — friluftsscen i Stadsträdgården med Cleo Petra Marklund Lilla spöket Laban
- **Ulva kvarn** — hantverksby från 1759 med glasblåseri silversmide café restaurang och nya Ulvabadet
- **Wiks slott** — medeltidsslott vid Mälaren med kojbyggarland i Wikparken och sommarguidning
- **Lövstabruk** — vallonbruksort med Barnens Bruk lekmiljö av Sven Nordqvist och Cahman-orgeln 1728

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Uppsala family-event ecosystem as of 2026-06-11.

Sources:
- [Linnéträdgården](https://destinationuppsala.se/activities/linnetradgarden/)
- [Botaniska trädgården](https://destinationuppsala.se/se-gora-ata/botaniska-tradgarden/)
- [Uppsala domkyrka visningar](https://www.svenskakyrkan.se/uppsaladomkyrka/visningar)
- [Takvandring på Uppsala slott](https://destinationuppsala.se/event/takvandring-pa-uppsala-slott-2026/)
- [Hågadalen-Nåstens naturreservat](https://www.uppsala.se/kultur-idrott-fritid/plats/friluftsomraden-naturreservat/hagadalen-nastens-naturreservat/)
- [Linnés Hammarby](https://destinationuppsala.se/se-gora-ata/linnes-hammarby/)
- [Bror Hjorths Hus](https://brorhjorthshus.se/utstallningar/)
- [Parksnäckan](https://parksnackan.se/)
- [Biotopia](https://biotopia.nu/)
- [Gustavianum](https://www.uu.se/en/gustavianum)
- [Ulva kvarn](https://destinationuppsala.se/activities/ulvakvarn/)
- [Wiks slott guidning](https://regionuppsala.se/wiks-slott/att-gora/guidning-sommaren-2026/)
- [Lövstabruk](https://destinationuppsala.se/event/en-dagsresa-till-lovstabruk/)
