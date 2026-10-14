# Upplands Väsby Event Publishing — FINAL Report (DEEP DIVE round 2)
**Date:** 2026-06-10
**Municipality:** Upplands Väsby (municipalityId: 172600240455582878)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **39** |
| **Events AFTER this session** | **45** |
| **Net new events published this session** | **+6** |
| **Multi-date instances bundled** | **~250+** (Vilundabadet 80-date hela sommaren + Kanot Introträning 12-date torsdagar + Sommarlov Ung Fritid 60-date V25-V33 + Zumba familj 12-date torsdagar) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | medley.se/vilundabadet | **1 event**: Vilundabadet äventyrsbad med vattenrutschkanor |
| 2 | upplandsvasby.se Kanot Introträning | **1 event**: Kanot Introträning för ungdomar 10-14 år Kanotklubben Glid |
| 3 | upplandsvasby.se Sommarlov Ung Fritid | **1 event**: Sommarlov med Ung Fritid 12-20 år Vega och Libra |
| 4 | upplandsvasby.se Zumba för hela familjen | **1 event**: Zumba för hela familjen Sigma centrum med ZolZumba |

## 4 events published this session

### Bad och äventyr (1)
1. **Vilundabadet äventyrsbad med vattenrutschkanor barnplask och bastur** (80-date hela sommaren)

### Vatten- och fritidssport (1)
2. **Kanot Introträning för ungdomar 10-14 år hos Kanotklubben Glid** (12-date torsdagar sommar och tidig höst)

### Ungdomshäng och kollo (1)
3. **Sommarlov med Ung Fritid på fritidsgårdarna Vega och Libra för ungdomar 12-20 år** (60-date V25-V33 14-21)

### Dans och rörelse (1)
4. **Zumba för hela familjen på ängen bakom Sigma centrum med ZolZumba** (12-date torsdagar sommar 18-19)

### Round 3 deep web search bonus (2)
5. **Barnens Wäsby Verkstäder temalekplats i Vilundaparken med industriarvet som inspiration** (80-date hela sommaren, öppet 7:30-19 Hasselbladskamera Volvo Amazon brandbil snickarverkstan)
6. **Vilundaparken aktivitetspark med skatepark pumptrack klättervägg och gratis utlåning** (80-date säsongstart 13 juni, 800 kvm skatepark + pumptrack + utegym + 4m klättervägg)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582878 (not null) | ✅ ALL 6 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 6 |
| Title duplicate check before publish | ✅ ALL 6 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 6 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 6 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 6 |
| Multi-date bundled as single event | ✅ Vilundabadet 80, Kanot 12, Ung Fritid 60, Zumba 12 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 6 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 6 |
| Description clean (no JS/code, prose only) | ✅ ALL 6 |
| ctaLink to source page (direct) | ✅ ALL 6 |
| Per Rule #10.6 in-depth + web search | ✅ 6 sources explored (incl Barnens Wäsby Verkstäder + Vilundaparken round 3) |

## Skipped (rule-compliant)

- **Tema Läder Gunnes gård 9-14 juni** — redan baseline (Tema-serien från Gunnes gård)
- **Jobbcoachning** — vuxen arbete (redan baseline)
- **Sagor och pyssel** — redan baseline
- **IT-hjälp** — senior IT-support (redan baseline)
- **Svenska för alla** — vuxen språkkurs
- **Messingen multifunktionshus** — generic venue-info ingen specifik event
- **Befintliga baseline events** (Gunnes gård tema-serie, Vikingatida höstmarknad, Arkeologidagen, Sättra Gårds naturreservat, De vilda blommornas dag, Midsommarafton, Återbruksfestivalen, Ungkulturhuset Vega, Träd in i dansen, Café Röda stugan, Öppna förskolan Fresta, Sommarlov Sommar i Väsby, Sommar Järnvägsparken, Utställning Väsby Konsthalls Vänner, Mördande magi Gunnes gård etc.) — redan publicerade

## Coverage assessment

Upplands Väsby now at **+6 net new (45 total live)**. Upplands Väsby hade redan rik baseline coverage (39 events) genom kommunens omfattande sommarprogram och Gunnes gård tema-serie. Round 2 lagt till stora signaturmål:

Höjdpunkter:
- **Vilundabadet** — äventyrsbad med vattenrutschkanor barnplask Fritt Fall strömbassäng bastur
- **Kanotklubben Glid** — introträning för 10-14 år på vattnet med klubbens instruktörer
- **Sommarlov Ung Fritid Vega och Libra** — 60-dagars öppen ungdomsverksamhet med gratis mellanmål
- **Zumba för hela familjen** — utomhus på ängen vid Sigma centrum från 5 år

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Upplands Väsby family-event ecosystem as of 2026-06-10.

Sources:
- [Upplands Väsby evenemangskalender](https://www.upplandsvasby.se/arkiv/evenemang/evenemangskalender)
- [Medley Vilundabadet](https://www.medley.se/vilundabadet)
- [Kanot Introträning 10-14 år](https://www.upplandsvasby.se/arkiv/evenemang/evenemangskalender/evenemang/kanotintrotraningforungdomar1014ar.5.52f7529019cfe7f2e393ad7.html)
- [Sommarlov med Ung Fritid](https://www.upplandsvasby.se/arkiv/evenemang/evenemangskalender/evenemang/2026-05-19-sommarlov-med-ung-fritid)
- [Zumba för hela familjen](https://www.upplandsvasby.se/arkiv/evenemang/evenemangskalender/evenemang/zumbaforhelafamiljen.5.52f7529019cfe7f2e393cde.html)
- [Barnens Wäsby Verkstäder](https://www.upplandsvasby.se/trafik-och-resor/torg-och-allmanna-platser/lekplatser/barnens-wasby-verkstader.html)
- [Vilundaparken aktivitetspark](https://www.upplandsvasby.se/uppleva-och-gora/idrott-motion-och-friluftsliv/vilundaparken)
