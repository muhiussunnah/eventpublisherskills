# Vaxholm FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-22
**Municipality:** Vaxholm (municipalityId: 172600240455582880)

## Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **30** |
| **Live events AFTER** | **34** |
| **Net new events published** | **+4** |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | destinationvaxholm.se/sv/kommande-evenemang | 28 events listed — most DUPs (bäversafari, kajakpaddling med fika, 100-års jubileum, musik i sommarkväll, paranormal afton, hembygdsförening, skärgårdsmarknad) |
| 2 | vaxholm.se/uppleva--gora/evenemang (3 pages, 13 events) | 4 NEW published |
| 3 | tickster.com vaxholm | **0** — "Tyvärr, vi hittade inga evenemang" (empty calendar) |
| 4 | svenskakyrkan.se Vaxholm | **0** — generic kalender page only |
| 5 | ticketmaster Vaxholm | **0** — no Vaxholm-specific events |
| Web search bonus | Wild Camp, Kastelletbåten, escape room | Found but need follow-up sources |

## 4 NEW events published

1. **Sagostund på Lägret med bibliotekets barnavdelning** — 3 dates (9, 16, 23 juli) — Lägret Hamngatan, fri entré, barn 0-17 år
2. **Utebio på Rindö redutt** — 22 augusti, Folk och rövare i Kamomilla stad (13.00) + Sentimental value (16.00), fri entré
3. **Countryfestival på kajen i Vaxholm med Wildwood Country Music Fest** — 22 augusti 15-21, Hamngatan 2, 325 kr (barn under 12 gratis)
4. **Vaxholms kulturnatt** — 9-10 oktober, musik dans teater konst på flera platser, fri entré

### Failed (1)
- Kajakpaddling med ö-lunch — image URL 404 (no good source image), kunna behöva källfetch och ny image

## Rules compliance verification ✅

| Rule | Result |
|---|---|
| municipalityId not null (Vaxholm 172600240455582880) | ✅ ALL 4 |
| Image present (no image = no publish) | ✅ ALL 4 (source images from vaxholm.se) |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 4 |
| Title duplicate check against live (30 events) | ✅ 7 dups detected and skipped |
| Multi-date bundled (Sagostund 3 dates, Kulturnatt 2 dates) | ✅ |
| Only active/upcoming dates (today 2026-06-22+) | ✅ ALL 4 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 4 |
| Clean prose descriptions (no JS/code, source-accurate) | ✅ ALL 4 |
| ctaLink to source page | ✅ ALL 4 |
| Pagination processed (vaxholm.se 3 pages, destinationvaxholm full list) | ✅ |

## Skipped (dup with live)

- Utställning Hembygdsföreningen Byggnader (already published as "Vaxholms Hembygdsgård...")
- Bäversafari med kanot — DUP
- Kajakpaddling med fika — DUP
- 100-års jubileum Pålsundsbron — DUP
- Promenadteater i Vaxholm — DUP
- Musik i sommarkväll konsertserie — DUP
- Paranormal afton Bogesunds slott — DUP
- Skärgårdsmarknad och Strömmingsrodd — DUP
- Sommarens visningar av Ytterby gruva — DUP
- Hemligt uppdrag spionernas värld — DUP
- Få hjälp med jobb, studier och ekonomi — vuxenfokus, ej familj

## Sources

- [destinationvaxholm.se kommande evenemang](https://www.destinationvaxholm.se/sv/kommande-evenemang)
- [vaxholm.se evenemang page 1](https://www.vaxholm.se/uppleva--gora/evenemang)
- [Sagostund på Lägret](https://www.vaxholm.se/uppleva--gora/evenemang/evenemang-/2026-06-17-sagostund-pa-lagret)
- [Utebio på Rindö redutt](https://www.vaxholm.se/uppleva--gora/evenemang/evenemang-/2026-06-17-utebio-pa-rindo-redutt)
- [Countryfestival på kajen](https://www.vaxholm.se/uppleva--gora/evenemang/evenemang-/2026-06-17-countryfestival-pa-kajen)
- [Vaxholms kulturnatt](https://www.vaxholm.se/uppleva--gora/evenemang/evenemang-/2026-06-17-vaxholms-kulturnatt)
