# Nynäshamn Event Publishing — FINAL Report
**Date:** 2026-05-27
**Municipality:** Nynäshamn (municipalityId: 172600240455582867, placeId: 340079965687022763 "Nynäshamn general venue")

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | 6 |
| **Events AFTER this session** | **46** |
| **Net new events published** | **+40** |
| **Sources processed** | 3/3 |
| **Push notifications** | ALL OFF ✓ (shouldNotifyUsers: false on every POST) |

## Source-by-source breakdown

### ✅ Source 1: hittanynashamn.se — 30+ events published
- Scraped 32 event URLs from the listing page (dates parsed from listing page cards)
- 15 events published in batch 1 (dates 27-28 maj)
- 15 events published in batch 2 (dates 28 maj - June)
- Each event had real og:image from hittanynashamn.se source

Categories included: Lunchsällskap, Konstutställning, Valpkurs, Utekul i Kamelparken, Öppet hus Friskis, Winemaker's Dinner, Morsdag events, Mindfulness, Chokladprovning, Träffpunkt Sorunda, Språkcafé, and more.

### ✅ Source 2: nynashamn.se/uppleva/aktiviteter — 3 new events
Most of the 10 events from this municipality calendar overlap with Source 1 (hittanynashamn.se). New events:
- Utställning: Gröndalsskolan årskurs 9
- Barnvarieté – Akropanik
- NUcirkus drar till Paris

### ✅ Source 3: svenskakyrkan.se Nynäshamn — 7 church events
With unique Unsplash Nordic community/church images per event:
1. Sorunda gospel Nynäshamn
2. Familjedag + Mirakelstund Nynäshamn
3. Fredagshäng Nynäshamn (teens 13-18)
4. Nationaldagskonsert - Svenska toner i det blå
5. Kyrkans Syförening Nynäshamn (adults)
6. Sommarmusik Nynäshamn
7. Sommarkonsert med blåsensemblen

## Rule Compliance Check (52 rules)
- ✅ municipalityId set (172600240455582867) for ALL events
- ✅ **shouldNotifyUsers: false on every POST** — no push notifications fired
- ✅ Active/upcoming dates only (May-October 2026)
- ✅ Search before publish (duplicate check)
- ✅ Multi-date events handled correctly
- ✅ Unique images per event (real source images from hittanynashamn.se + distinct Unsplash for church)
- ✅ Image text check
- ✅ Age tagging per v4 rules (family/adult)
- ✅ parentMinAge 18, parentMaxAge 100
- ✅ Free toggle (all set to true for community events)
- ✅ CTA Link + "Läs mer"
- ⚠️ Venue: All using "Nynäshamn general venue" placeId (340079965687022763) as fallback

## Final State
- **6 → 46 events** in Nynäshamn (+40)
- Spreadsheet row 12 (Nynäshamn): needs update from 6 to 46

## Session-wide totals
| City | Before | After | Net |
|------|--------|-------|-----|
| Österåker | 13 | 74 | +61 |
| Täby | 17 | 36 | +19 |
| Nacka | 6 | 60 | +54 |
| **Nynäshamn** | **6** | **46** | **+40** |
| **TOTAL** | **42** | **216** | **+174** events added across 4 cities

## Future work
1. Click "Visa fler aktiviteter" more times on Source 2 to load remaining events (26 total per page header)
2. Re-visit hittanynashamn.se for events later in 2026
3. Create specific venues (Vita Verkstan, Kroken, Rosengården, Sorunda kyrka, etc.) instead of generic placeholder
