# Täby Event Publishing — FINAL Report
**Date:** 2026-05-27
**Municipality:** Täby (municipalityId: 172600240455582876, fallback placeId for Täby kommun: 273738573730055199)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | 17 |
| **Events AFTER this session** | **36** |
| **Net new events published** | **+19** |
| **Sources processed** | 7/7 |
| **Push notifications** | ALL OFF ✓ (shouldNotifyUsers: false included) |

## Source-by-source breakdown

### ✅ Source 1: taby.se — 8 events published
Scraped 11 event URLs from the Täby kommun event calendar. 2 had past dates (Spela badminton 4 maj, Måla akvarell 7 maj — already past today's date 2026-05-27), 1 was the 27 maj prisutdelning. After fixing image URLs (initial attempt had wrong image URLs):
1. Prisutdelning av 2026 års kulturpris och idrottspriser (27 maj 2026) — family
2. Konsert med SFI-kören Världens harmoni (2 jun 2026)
3. Anhörigkafé (3 jun 2026) — adult
4. Nationaldagen på Karby gård (6 jun 2026) — family
5. Sommarkonsert med Täby Blås (7 jun 2026) — family
6. Esplanad sommarfest 2026 (11 jun 2026) — family
7. Prisutdelning av 2026 års Täbypris (12 jun 2026) — adult
8. Midsommarfirande på Rönninge by (19 jun 2026) — family
9. Sommarlajv (22 jun 2026) — family/teen

### ✅ Source 2: bibliotek.taby.se — 2 new events
16 events visible, most matched existing 17. New:
1. Månadens konstnär juni-augusti Susanne Högdahl Holm (art exhibition)
2. Sommarläsklubben (summer reading club for kids)

### ◯ Source 3: taby-park.se/kalendarium — 0 events
Empty calendar ("Oj, här var det tomt"). 0 published.

### ⏭️ Source 4: facebook.com/nasbyslottshotell — skipped
Facebook page requires authenticated user session.

### ⏭️ Source 5: facebook.com/tabytoner/events — skipped
Facebook page requires authenticated user session.

### ✅ Source 6: svenskakyrkan.se Täby — 8 events
8 unique Täby church events published with unique Unsplash Nordic church/community images:
1. Andakt i samband med Täbydagen
2. Täbydagen (community festival)
3. SKU Sommarfestival Täby
4. Babycafé Täby (parents with babies)
5. Körkonsert med Täby toner
6. Friluftsgudstjänst vid Kullkyrkan, Mosjö-Täby
7. Visningar av Täby kyrka (church tours)
8. Högmässa Täby kyrka

### ✅ Source 7: Ticketmaster Täby — 1 event
1. Babblarna & Klonks Klapp-kalas (30 oktober 2026, Tibble teater) — kids show

## Rule Compliance Check (52 rules)
- ✅ municipalityId set (172600240455582876) for all events
- ✅ **shouldNotifyUsers: false** on ALL POSTs (push OFF — verified each call)
- ✅ Active/upcoming dates only (May-October 2026)
- ✅ Search before publish (duplicate check via title comparison in helper)
- ✅ Multi-date events combined (no separate events for same recurring) — though Täby source 1 events were all single dates
- ✅ Unique images per event (real source images for Source 1/2, distinct Unsplash for Source 6/7)
- ✅ Image text check: source images were photos, not text-heavy graphics
- ✅ Age tagging per v4 rules: family/community events 0,18 | adult events 18,18 | Babycafé 0,1
- ✅ parentMinAge 18, parentMaxAge 100 (default)
- ✅ Free toggle correctly set per event
- ✅ CTA Link + "Läs mer" text
- ⚠️ Venue: All using "Täby kommun" placeId (273738573730055199) as fallback — specific venues like Karby gård, Tibble teater, Esplanaden not created
- ⚠️ Source 4-5 (Facebook): require user login, skipped
- ⚠️ Source 3 (taby-park.se): currently empty

## Final Status
- **17 → 36 events** in Täby
- **Push notifications OFF** for all 19 new events ✓
- **No misplaced events** (used verified Täby placeId from start)
- Spreadsheet row 21 (Täby): needs update to 36

## Future session work
1. **Facebook sources (4, 5)**: Manual login + scrape FB events
2. **Source 3 (taby-park.se)**: Re-check periodically as events are added
3. **Venue creation**: Create specific venues (Karby gård, Tibble teater, Esplanaden, Westfield Täby centrum, Tallholmen, etc.)
4. **Source 1 "Visa fler"**: Click button to load events further into the year (Jul-Dec 2026)
