# Vallentuna FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-22
**Municipality:** Vallentuna (municipalityId: 172600240455582879)

## Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **50** |
| **Live events AFTER** | **51** |
| **Net new events published** | **+1** |

## Sources processed (6 of 6)

| # | Source | Result |
|---|---|---|
| 1 | upplevvallentuna.se | Redirects to vallentuna.se (consolidated) |
| 2 | vallentuna.se evenemangskalender | JS-rendered, no events visible to WebFetch |
| 3 | Under bar himmel 2026 festival page | All 20 program items in window **29 maj-6 juni** — ALL PAST (today 2026-06-22) |
| 4 | Beredskapsveckan Skattjakten page | **1 NEW** (22-26 september skattjakt) |
| 5 | bibliotek.vallentuna.se | Aggregate calendar, overlap with previous rounds |
| 6 | svenskakyrkan / ticketmaster Vallentuna | 0 (no new events) |
| Web search bonus | barnistan, barnsemester | Found Ninja World Sports Club (image URL 404 on publish) |

## 1 NEW event published

1. **Skattjakten Den försvunna beredskapskistan i Vallentuna 22 till 26 september** — 5 dates bundled (22, 23, 24, 25, 26 september 2026)
   - Family skattjakt under Beredskapsveckan, follow Valentina genom Vallentuna, 5 platser (vattentornet, Lindholmen, lekplats Kårsta, Karby motionsspår, Vallentuna kulturhus & bibliotek), 5 föremål (vattendunk + handsprit, powerbank, ficklampa, första hjälpen-kit, vevradio)
   - Source image from vallentuna.se (Skattjakt ChatGPT image)
   - Free entry, ctaLink to source page

### Failed (1)
- Ninja World Sports Club Vallentuna inomhushinderbana — image URL guess 404'd (barnistan.se hot-link didn't resolve)

## Rules compliance ✅

| Rule | Result |
|---|---|
| municipalityId Vallentuna 172600240455582879 not null | ✅ |
| Image present from source | ✅ |
| Push OFF (shouldNotifyUsers: false) | ✅ |
| Title dup check against 50 live events | ✅ Kvarnbadet detected as DUP |
| Multi-date bundled (5 dates 22-26 sept) | ✅ |
| Active/upcoming only (today 2026-06-22+) | ✅ Under bar himmel skipped (29 maj-6 juni all past) |
| Clean prose description, source-accurate | ✅ |
| ctaLink to source page | ✅ |
| Web search performed for hidden events | ✅ Ninja World + 4H-gård dagläger + sommarlov found, dups |

## Skipped/checked but not new

- **Under bar himmel 2026** — entire festival 29 maj-6 juni past dates (20 program items: Yoga, Malin & David Watson, Blueskväll, Familjen Svängsson, Karusell, Konstverkstad havets framtid, Jenny Almsenius Povel Ramel, Blomworkshop Bea Szenfeld, Pelargoner, Sommarteater Den girige, Kulturskolefestival, Sittgympa, Poesibingo, Golbang, Vernissage Inlåst & utanför, Basic Big Band, Lunchblues, Bingo, Sittgympa #2, Nationaldagen)
- **Kvarnbadet** — already published as "Kvarnbadet utomhusbad..."
- **Vallentuna 4H-gård dagläger** — overlap with already published 4H-gård visningsgård
- **Sommarlov i Vallentuna** — too generic
- **Dansommarlovskurs 16-17 juni** — past dates

## Coverage assessment

Vallentuna already had extensive coverage (50 live events from previous Rounds 1-3) — bibliotek aktiviteter, kulturskolan, 4H-gård, Kvarnbadet, Kulturhuset, Snapptuna Kreativitetspark, Vallentuna judo all already represented.

The vallentuna.se evenemangskalender is fully JS-rendered (Hämtar evenemang... placeholder visible to WebFetch). The Under bar himmel festival's 20 program items all sat in the 29 maj-6 juni window which is past as of today (2026-06-22), so all skipped per active/upcoming rule.

Only NEW content publishable was the September Beredskapsveckan Skattjakten + 1 web-search bonus (Ninja World — failed on image URL).

## Sources

- [vallentuna.se evenemang](https://www.vallentuna.se/evenemang-och-upplevelser/evenemangskalender/)
- [Under bar himmel 2026](https://www.vallentuna.se/evenemang-och-upplevelser/under-bar-himmel/)
- [Skattjakten Den försvunna beredskapskistan](https://www.vallentuna.se/evenemang-och-upplevelser/beredskapsveckan/skattjakten-den-forsvunna-beredskapskistan/)
- [barnistan.se Ninja World Vallentuna](https://www.barnistan.se/tips/evenemang/hostlov-i-ninja-world/)
