# Vaxholm Event Publishing — FINAL Report
**Date:** 2026-05-27
**Municipality:** Vaxholm (municipalityId: 172600240455582880, placeId: 339626367891047479 "Vaxholm general venue")

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | 19 |
| **Events AFTER this session** | **43** |
| **Net new events published** | **+24** |
| **Sources processed** | 5/5 |
| **Push notifications** | ALL OFF ✓ (shouldNotifyUsers: false on every POST) |
| **Rule audit** | 0 issues / 43 events |

## Source-by-source breakdown

### ✅ Source 1: vaxholm.se kommun events — 6 new
All 3 pagination pages (15 events total) scraped. New (non-duplicate, upcoming):
1. Rock Night på Storstugan (27 maj)
2. Scouternas loppis på Rådhustorget i Vaxholm (30 maj)
3. Få hjälp med jobb, studier och ekonomi i Vaxholms rådhus (2 jun)
4. HBTQI-satsning för unga i Vaxholm (2 jun)
5. Workshop för barn på Vaxholms bibliotek (12 jun)
6. Traditionsenligt midsommarfirande i Vaxholm (19 jun)

### ✅ Source 2: destinationvaxholm.se — 3 new (multi-date)
67 unique events listed; most already covered or past. New events:
1. **Bäversafari med kanot i solnedgången** (multi-date: 27 maj, 10 jun, 24 jun, 8 juli, 22 juli, 12 aug, 26 aug, 9 sep — 8 dates as 1 event)
2. Militärhistorisk specialvisning på Oscar-Fredriksborgs fort (7 jun)
3. **Paranormal afton på Bogesunds slott** (multi-date: 12 sep, 17 okt, 14 nov — 3 dates as 1 event)

### ✅ Source 3: svenskakyrkan.se Vaxholm — 6 new
1. Nationaldagskonsert med Svenska Lyxorkestern och Vaxholms kyrkokör (6 jun)
2. **Fika och gemenskap på kyrkbacken** (multi-date: 12 dates jun-aug)
3. Sommaröppet med guidning och loppis i Vaxholms kyrka (22 jun-28 aug)
4. **Söndagsskola i Vaxholms kyrka** (multi-date: 4 söndagar)
5. **Handarbetscafé i gamla brandstationen** (multi-date: 6 tisdagar)
6. **Sommarretreat i Vaxholms församling** (multi-date: 3 tisdagar i juli)

### ✅ Source 4: vaxholmsfastning.se (Vaxholms Fästnings Museum) — 6 new
1. **Guidade turer på Vaxholms Kastell** (multi-date: 51 dagar 27 jun-16 aug)
2. Hemligt uppdrag! En dag i spionernas värld (5 juli)
3. Guidad visning på Oscar-Fredriksborgs fort – nedre verket (9 aug)
4. Militärhistorisk vandring på Fredriksborgs fästning (27 sep)
5. Kulturnatt i oktober på Vaxholms Fästnings Museum (9 okt)
6. **Höstlovsöppet på Vaxholms Fästnings Museum** (multi-date: 24-26 okt)

### ✅ Source 5: bibliotek + roddarhuset + ticketmaster — 3 new
1. **Lördagspyssel på Vaxholms bibliotek** (multi-date: 26 lördagar)
2. Utställning fågelholkar på Vaxholms bibliotek (18-31 maj)
3. **Släktforskningsjour på Vaxholms bibliotek** (multi-date: 4 träffar sept-okt)

⛔ Ticketmaster Vaxholm: 0 results

## Rule Compliance — Verified via detail API audit on all 43 events

| Rule | Status |
|---|---|
| shouldNotifyUsers: false on every POST | ✅ ALL 43 |
| municipalityId 172600240455582880 set | ✅ ALL 43 |
| placeId 339626367891047479 set (no null) | ✅ ALL 43 |
| Active/upcoming dates only (≥ 27 maj 2026) | ✅ ALL 43 |
| Title duplicate check before publish | ✅ ALL 43 (verified across pages 1-3) |
| Multi-date as single event (no separate events) | ✅ 9 multi-date events |
| Unique images per event | ✅ 0 new duplicates (pre-existing dup from session #1) |
| Image text check (PNG with text → Unsplash replacement) | ✅ Drop-in coach PNG, Solros.png swapped |
| Age tagging per v4 rules | ✅ family 0,18 \| adult 18,18 \| barn 3-12 \| ungdom 13-18 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 43 |
| Free toggle set per event | ✅ ALL 43 |
| CTA Link + "Läs mer" text | ✅ ALL 43 |
| Real source images where available | ✅ vaxholm.se, destinationvaxholm.se SquareSpace CDN, svenskakyrkan |

## Multi-date events summary (per rule "multiple date thakle 1tar under e publish korba")
| Event | Dates | Date range |
|---|---|---|
| Bäversafari med kanot i solnedgången | 8 | 27 maj - 9 sep |
| Paranormal afton på Bogesunds slott | 3 | 12 sep - 14 nov |
| Fika och gemenskap på kyrkbacken | 12 | 8 jun - 18 aug |
| Söndagsskola i Vaxholms kyrka | 4 | 31 maj - 21 jun |
| Handarbetscafé Vaxholm | 6 | 2 jun - 15 sep |
| Sommarretreat i Vaxholms församling | 3 | jul tisdagar |
| Guidade turer på Vaxholms Kastell | 51 | 27 jun - 16 aug |
| Höstlovsöppet Fästnings Museum | 3 | 24-26 okt |
| Lördagspyssel på Vaxholms bibliotek | 26 | varje lördag |
| Släktforskningsjour på biblioteket | 4 | 5 sep - 17 okt |
| **TOTAL date-instances bundled into 10 events** | **120** | |

## Session-wide totals (7 cities)
| City | Before | After | Net |
|------|--------|-------|-----|
| Österåker | 13 | 74 | +61 |
| Täby | 17 | 36 | +19 |
| Nacka | 6 | 60 | +54 |
| Nynäshamn | 6 | 46 | +40 |
| Tyresö | 4 | 18 | +14 |
| Uppsala | 19 | 127 | +108 |
| **Vaxholm** | **19** | **43** | **+24** |
| **TOTAL** | **84** | **404** | **+320 events added!**

## Future session work
1. Bogesunds slott has more events at bogesundsslott.se (paranormal afton publiserad, finns andra)
2. Vaxholms Stadshotell, Vaxholms Hotell — privata venuer
3. Strömmingsroddarna utställning (april) — närmare till säsong
4. Visning på Rindö, Skarpö, Tynningö ö-vandringar
5. Create specific venues (Vaxholms Kastell, Bogesunds slott, Oscar-Fredriksborgs fort, Storstugan, Rådhustorget) istället för placeholder
