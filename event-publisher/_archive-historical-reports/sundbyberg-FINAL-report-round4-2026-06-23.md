# Sundbyberg FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-23
**Municipality:** Sundbyberg (municipalityId: 172600240455582873)

## 🎯 Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **15** |
| **Live events AFTER** | **28** |
| **Net new events published** | **+13** |

## 📊 13 NEW Sundbyberg events published

### Fritid (2)
1. **Passa Vidare på Rissne IP** — 10 weekdays vecka 25-27, 12-17.30 (Fritid Sundbyberg + Sundbybergs IK)
2. **Barnens Dag på Rissne IP** — 26 juli 12-17 (hoppborgar, trollkar)

### Kulturskolan / Kulturcentrum (5)
3. **Keramik och skulptur sommarworkshop** — 23, 24 jun + 14 aug (15-25 år)
4. **Sommartorget i Hallonbergen Centrum** — 9 weekdays vecka 26-27, 12-16 (dans, cirkus, musik, skapande)
5. **Pop up workshop med Aggregat** — 9 dates juni-juli i parker (6-17 år)
6. **Hallonbergen Summerjam DJ-ing och dans** — 29 + 30 juli (10-13 år och 14-18 år)
7. **Prova på spelskapande och ljuddesign** — 28-31 augusti vecka 36 (10-15 år)
8. **Pianoläger** — 3-6 aug (8-12 år) + 10-13 aug (12-20 år)

### Bibliotek (4)
9. **Bokskattjakt** — 14 presentböcker gömda runt Sundbyberg, vecka 25-27
10. **Pyssel på bibblan** — vecka 25-27 + 31-33 från 6 år
11. **Sommarboken UNG** — 15 juni-31 augusti (13-20 år) läs 3 böcker → få bok
12. **Kom och häng med biblioteket på Sommargågatan Centralvägen** — 10 juni-26 augusti (ej 29 juli + 5 aug)

### Teater (1)
13. **Biografmysteriet LasseMajas Detektivbyrå** Teater Bristol — 29 aug-15 nov (5-11 år)

## 📋 Sources processed

| # | Source | Result |
|---|---|---|
| 1 | sundbyberg.se evenemang-och-aktiviteter | Mostly Anhörig/Internethjälpen (adult) — 0 family NEW |
| 2 | sundbyberg.se Lovaktiviteter Sumpanlov page | **+12 NEW** (Fritiden + Kulturskolan + Bibliotek) |
| 3 | barnistan.se Solna/Sundbyberg | **+1 NEW** (Biografmysteriet LasseMajas) |
| 4 | Web search | Kom och häng med biblioteket (Centralvägen) — included |
| 5 | Marabouparken konsthall | Already covered (Konstkojor + Sagostund i live) |
| 6 | Signalfabriken | Already in live |
| 7 | bibliotek.sundbyberg.se | All bibliotek events covered above |

## ✅ Rules compliance

| Rule | Result |
|---|---|
| municipalityId Sundbyberg 172600240455582873 not null | ✅ ALL 13 |
| Image present (Sumpanlov source image from sundbyberg.se) | ✅ ALL 13 |
| Push OFF (shouldNotifyUsers: false) | ✅ ALL 13 |
| Title dup check against 15 live | ✅ DUPs detected (Sumpanlov/Konstkojor/Sagostund Marabouparken/Pop up Ursvik) skipped |
| Multi-date bundled (Passa Vidare 10d, Sommartorget 9d, Pop up Aggregat 9d, Pyssel 12d, Sommargågatan 40+d, LasseMajas 12d, Bokskattjakt 13d) | ✅ |
| Active/upcoming only (today 2026-06-23+) | ✅ ALL 13 |
| Clean prose descriptions, source-accurate | ✅ ALL 13 |
| ctaLink to source page | ✅ ALL 13 |
| Web search performed | ✅ Sumpanlov page + barnistan + tabynytt |

## Skipped (DUP with live or out of scope)

- Sumpanlov: Lovaktiviteter (DUP umbrella)
- Konstkojor Marabouparken (DUP)
- Sagostunder i Marabouparken (DUP — already published, source detail 16+23 juni)
- Pop up i Ursvik 16-23 juni (DUP — "Pop up i Ursvik – mobil biblioteksvagn" in live)
- God natt, Alfons Åberg (DUP)
- Sommarmusik i Sundbybergs kyrka (DUP)
- Plaskdammar/Lötsjön-Golfängarna/Sundbybergs simhall (DUPs as recurring venues)
- Internethjälpen 9 juli (adult tech help)
- Anhörigcirkel/grupp (adult)
- Sommarmusikanterna (turnerar äldreboenden — seniors)
- Pianoläger 15-18 juni (past)
- Fantasy Illustration 16-18 juni (past)

## Sources

- [sundbyberg.se Lovaktiviteter](https://www.sundbyberg.se/uppleva-och-gora/ung-i-sundbyberg/lovaktiviteter)
- [sundbyberg.se evenemang och aktiviteter](https://www.sundbyberg.se/arkiv/evenemang-och-aktiviteter)
- [barnistan.se Solna/Sundbyberg](https://www.barnistan.se/omrade/aktiviteter-barn-solna-sundbyberg/)
- [Biografmysteriet LasseMajas på Teater Bristol](https://www.barnistan.se/tips/evenemang/biografmysteriet-lassemajas-detektivbyra/)
