# Täby FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-23
**Municipality:** Täby (municipalityId: 172600240455582876)

## 🎯 Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **14** |
| **Live events AFTER** | **18** |
| **Net new events published** | **+4** |

## 📊 4 NEW Täby events published

1. **Fårhage med tre tackor och en ung bagge på Åkerbyparken** — 7 augusti 15.00 + 17.00 (klippning, utfodring, mjölkning som performance för familjen)
2. **Såpbubbleworkshop och prova-på-cirkus med Cirkus Cirkör** — 30 augusti 12-16, Åkerbyparken (jonglering, lindans, akrobatik)
3. **Klättertorn på Täby torg** — 45 dates 23 juni-6 augusti kl 13-17 (drop-in klättring för barn)
4. **Sommarlovsaktiviteter på Täby torg andra perioden** — 12 dates 28 juli-8 augusti kl 11-17 (pins, pärlplattor, måla tygkassar, värmeljushållare, nattduell, mega schack)

## 📋 Sources processed

| # | Source | Result |
|---|---|---|
| 1 | taby.se evenemangskalender / arkiv | 11 events listed, mostly Anhörig (adult) — 9 DUP, 0 NEW family |
| 2 | tabynytt.se kategori evenemang | 30+ events fetched — mostly past dates or adult-focused |
| 3 | Web search Sommarlovsaktiviteter på Täby torg | **+4 NEW** (Fårhage, Såpbubbleworkshop, Klättertorn, Sommarlov period 2) |
| 4 | Tibble teater 2026-27 program | Frukt och grönsaker (early sept past/upcoming TBD), Babblarna Klapp-kalas (DUP), Traditioner vid advent och jul (date TBD) |
| 5 | Rönninge by | Open hours only, no specific events |
| 6 | bibliotek.taby.se | JS-rendered, no events visible |
| 7 | Ticketmaster Täby | Already covered via existing live (Babblarna) |

## ✅ Rules compliance

| Rule | Result |
|---|---|
| municipalityId Täby 172600240455582876 not null | ✅ ALL 4 |
| Image present (Unsplash family-friendly imagery, no duplicates with existing) | ✅ ALL 4 |
| Push OFF (shouldNotifyUsers: false) | ✅ ALL 4 |
| Title dup check against 14 live | ✅ Sommarläsklubben/Sommarlajv/Täby spelmansstämma/Ung sommar pyssel DUPs detected and skipped |
| Multi-date bundled (Klättertorn 45 dates, Sommarlov P2 12 dates, Fårhage 2 shows same day) | ✅ |
| Active/upcoming only (today 2026-06-23+) | ✅ ALL 4 |
| Clean prose descriptions, source-accurate | ✅ ALL 4 |
| ctaLink to source page | ✅ ALL 4 |
| Web search performed | ✅ tabynytt.se + Tibble teater + Rönninge by |

## Skipped (DUP with live or adult)
- Sommarläsklubben (DUP)
- Sommarlajv (DUP)
- Pyssel och spel på torget (DUP with "Ung sommar med pyssel och spel på Täby torg")
- Täby spelmansstämma 2026 (DUP)
- Babblarna & Klonks Klapp-kalas (DUP)
- Friluftsgudstjänst vid Kullkyrkan (DUP)
- Månadens konstnär juni-augusti (DUP)
- Anhörigkafé / Anhörig grupp / Anhörig till Parkinsons / NPF / neurologisk sjukdom (5x adult/care)
- Navigeringskurs för anhöriga (adult)
- Musik och gemenskap (vague, likely seniors)
- Föräldraföreläsning fulsprit (adult only)

## Past dates skipped from tabynytt
Många events: Låtskrivarworkshop 15 juni, Prisutdelning 27 maj, Invigning tennisbanor 23 maj, Kulturskolans dagar 17 maj, Biljettsläpp 12 maj, Yrkes-SM 4-6 maj, Vårkonsert, Rocka sockor 21 mars, Tristan Isolde 21 mars, Kulturnatt 18 april — all in the past

## Sources

- [taby.se evenemangskalender](https://www.taby.se/arkiv/evenemang)
- [tabynytt.se evenemang](https://tabynytt.se/kategori/evenemang)
- [Sommarlovsaktiviteter på Täby torg (search)](https://www.taby.se/evenemang/fritid--kultur---evenemang/sommarlovsaktiviteter-pa-taby-torg/)
- [Tibble teater](https://www.taby.se/verksamhetswebbar/fritid-och-kultur/tibble-teater/evenemang-pa-tibble-teater-i-taby/)
- [Rönninge By](https://www.ronningeby.se/)
