# Tyresö FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-23
**Municipality:** Tyresö (municipalityId: 172600240455582875)

## 🎯 Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **28** |
| **Live events AFTER** | **41** |
| **Net new events published** | **+13** |

## 📊 13 NEW Tyresö events published

### Familjedagar (2)
1. **Familjelördag Vem räddar Alfons Åberg** — 19 september, Kulturcentrum Kvarnhjulet (från 4 år)
2. **Familjelördag Stockholm Jazz Festival familjekonsert** — 17 oktober, Kulturcentrum Kvarnhjulet

### Sommarlov 2026 recurring (3)
3. **Pyssel och annat kul med bibblan** — 19 dates vecka 26-27 + 32-33, Forelltorget/Biblioteket
4. **Sommar på Forelltorget** — 39 weekdays, Tyresö basket + sport + spel
5. **Öppet sommarkollo på G60** — 39 weekdays, Granängsringen 60 (sagoläsning, boule, multiarena)

### Bibliotek sommaraktiviteter (6)
6. **Sommarcafé på Bergfotens fritidsgård** — 25 jun + 2 juli
7. **Korsord vid stranden med Bibblabilen** — 26 juni, Strandbadet
8. **Sagostund med mysig rysare** — 29 juni, 3-6 år
9. **Bokträff för unga** — 30 juni
10. **Pop up K-pop** — 1 juli, Stadsparken
11. **Sommarbokenträff Mystiska gåtor och dolda spår** — 2 juli, 8-12 år
12. **Pop up One Piece** — 7 augusti, Fornuddsparken

### Special events (1)
13. **Bygg lego med en mästare Johan Bergman LEGO Masters** — 12 augusti, Forelltorget (150 kg LEGO)

## 📋 Sources processed

| # | Source | Result |
|---|---|---|
| 1 | tyreso.se Sommarlov 2026 page | 10 NEW + 5 DUPs detected |
| 2 | tyreso.se Familjedagar 2026 page | 2 NEW + 2 DUPs |
| 3 | bibliotek.tyreso.se | JS-rendered, content covered via Source 1 |
| 4 | tyresta.se (national park) | Only booking widget, no events fetched |
| Web search bonus | Tyresö slott family tours | DUP (already Familjevisning på Tyresö slott) |

## ✅ Rules compliance

| Rule | Result |
|---|---|
| municipalityId Tyresö 172600240455582875 not null | ✅ ALL 13 |
| Image present (source images from tyreso.se /images/) | ✅ ALL 13 |
| Push OFF (shouldNotifyUsers: false) | ✅ ALL 13 |
| Title dup check against 28 live | ✅ 9 DUPs detected and skipped |
| Multi-date bundled (Pyssel 19 dates, Sommar på Forelltorget 39 dates, Öppet sommarkollo 39 dates) | ✅ |
| Active/upcoming only (today 2026-06-23+) | ✅ ALL 13 |
| Clean prose descriptions, source-accurate from tyreso.se page text | ✅ ALL 13 |
| ctaLink to source/booking pages | ✅ ALL 13 |
| External URL approach (image upload API workaround) | ✅ ALL 13 |

## Skipped (DUP with live)
- Summer Challenge 135 (DUP)
- Familjevisning på Tyresö slott (DUP)
- Cirkusföreställning Unplugged med Johan Wellton (DUP)
- Familjelördag Giraffens ABC – Cirkusistanfestival (DUP)
- Välj väg ur dimman – interaktiv högläsning (DUP)
- Tyresö Novelltävling för 14-21 år (DUP)
- Therians och furries-träff (DUP)
- Warriors-boksamtal (DUP)
- Sagostund med pyssel 16 juni (past date)

## Sources

- [tyreso.se Sommarlov 2026](https://www.tyreso.se/uppleva--gora/kultur-och-fritid-for-barn-och-unga/sommarlov-2026.html)
- [tyreso.se Familjedagar](https://www.tyreso.se/uppleva--gora/kultur-och-noje/kultur-i-tyreso/familjedagar.html)
- [bibliotek.tyreso.se lovaktiviteter](https://bibliotek.tyreso.se/lovaktiviteter)
- [tyresta.se nationalpark](https://tyresta.se/)
