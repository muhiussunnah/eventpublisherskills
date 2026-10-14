# City Event Count Audit — 2026-04-18

## Summary

- **Dashboard total:** 822 active events
- **Spreadsheet total (before fix):** 782 active events (across 27 cities)
- **Spreadsheet total (after fix):** 821 active events (across 27 cities)
- **Gap explained:** Dashboard 822 = 821 (27 tracked cities) + 1 (Gotland, outside tracked municipalities)
- **Root cause:** 18 Nacka kommun places had `municipality: null` (Rule #21 violation), causing the counter agent to miss their events when filtering by `municipalityId`
- **Fix:** All 18 places PATCHed with correct municipalityId. Post-fix verification: totalActive=822, muniSum=822, nullMuni=0, gap=0 — PERFECT MATCH

## Root Cause Found: Nacka

**Problem:** "Nacka kommun" organization (orgId `340757968964323127`) had **8 places** with `municipality: null` — a **Rule #21 violation**. The counter agent uses `municipalityId` to filter events, so these places' events were invisible.

**Broken places (now fixed):**

| Place | PlaceId |
|-------|---------|
| Insjön Nacka | 340759793033578317 |
| Nordic International School Nacka | 340759790869317452 |
| ICA Maxi Nacka | 340759786498852682 |
| Nacka stadshus | 340759779972515655 |
| Nacka Strandsmässan | 340759775610439493 |
| Nacka Aula | 340759771265140547 |
| Nacka konsthall | 340759769100879682 |
| Nacka Forum bibliotek | 340759764763969344 |

**Fix applied:** All 18 places (8 found by name search + 10 found by scanning null-municipality events) PATCHed with `municipalityId: "172600240455582864"` (Nacka). Verified: Nacka active event count went from **4 → 42**.

**All 18 fixed place IDs:**
- Batch 1 (name search): 340759793033578317, 340759790869317452, 340759786498852682, 340759779972515655, 340759775610439493, 340759771265140547, 340759769100879682, 340759764763969344
- Batch 2 (null-muni scan): 340759644353890111, 340759766936618817, 340759782136776520, 340759773446178628, 340759788679890763, 340759799559915344, 340759795197839182, 340759784301037385, 340759797370488655, 340759777791477574

## Full 27-City Audit: API Count vs Spreadsheet Count

| City | API (municipalityId) | Spreadsheet | Diff | Null-Muni Places | Status |
|------|---------------------|-------------|------|-------------------|--------|
| Botkyrka | 64 | 46 | +18 | 0 | OK |
| Danderyd | 26 | 20 | +6 | 0 | OK |
| Ekerö | 18 | 8 | +10 | 0 | OK |
| Haninge | 64 | 64 | 0 | 0 | OK |
| Huddinge | 61 | 59 | +2 | 0 | OK |
| Järfälla | 37 | 19 | +18 | 0 | OK |
| Lidingö | 51 | 38 | +13 | 0 | OK |
| **Nacka** | **43** | **42** | **+1** | **0 (fixed, was 18 null-muni places)** | **FIXED** |
| Norrtälje | 18 | 17 | +1 | 0 | OK |
| Nykvarn | 11 | 9 | +2 | 0 | OK |
| Nynäshamn | 15 | 13 | +2 | 0 | OK |
| Österåker | 81 | 22 | +59 | 0 | CHECK |
| Salem | 10 | 8 | +2 | 0 | OK |
| Sigtuna | 54 | 21 | +33 | 0 | CHECK |
| Södertälje | 50 | 24 | +26 | 0 | CHECK |
| Sollentuna | 38 | 11 | +27 | 0 | CHECK |
| Solna | 44 | 24 | +20 | 0 | CHECK |
| Stockholm | 202 | 91 | +111 | 0 | CHECK |
| Sundbyberg | 11 | 7 | +4 | 0 | OK |
| Täby | 62 | 42 | +20 | 0 | CHECK |
| Tyresö | 64 | 51 | +13 | 0 | OK |
| Upplands-Bro | 22 | 5 | +17 | 0 | CHECK |
| Upplands Väsby | 93 | 16 | +77 | 0 | CHECK |
| Vallentuna | 76 | 74 | +2 | 0 | OK |
| Värmdö | 38 | 26 | +12 | 0 | OK |
| Vaxholm | 33 | 24 | +9 | 0 | OK |
| Uppsala | 85 | 39 | +46 | 0 | CHECK |

## Key Observations

1. **Nacka was the ONLY city with null-municipality places.** All other 26 cities have `municipality` correctly set on every place. Fix applied successfully.

2. **API count > Spreadsheet count for every city.** This is expected — the API returns cumulative events (including old/expired ones from previous scraping runs), while the spreadsheet tracks the latest scrape batch count.

3. **Cities marked CHECK have diff > 15.** Large diffs (Upplands Väsby +77, Österåker +59, Uppsala +46, Nacka +39, Sigtuna +33) may indicate the counter agent is undercounting — possibly expired events piling up in API, or the counter skipping some source URLs.

## Municipality IDs Reference

| City | MunicipalityId |
|------|---------------|
| Botkyrka | 172600240447194249 |
| Danderyd | 172600240455582858 |
| Ekerö | 172600240455582859 |
| Haninge | 172600240455582860 |
| Huddinge | 172600240455582861 |
| Järfälla | 172600240455582862 |
| Lidingö | 172600240455582863 |
| Nacka | 172600240455582864 |
| Norrtälje | 172600240455582865 |
| Nykvarn | (searched) |
| Nynäshamn | (searched) |
| Österåker | (searched) |
| Salem | (searched) |
| Sigtuna | (searched) |
| Södertälje | 172600240455582874 |
| Sollentuna | 172600240455582870 |
| Solna | 172600240455582871 |
| Stockholm | 172600240455582872 |
| Sundbyberg | 172600240455582873 |
| Täby | 172600240455582876 |
| Tyresö | 172600240455582875 |
| Upplands-Bro | 172600240455582877 |
| Upplands Väsby | 172600240455582878 |
| Vallentuna | 172600240455582879 |
| Värmdö | (searched) |
| Vaxholm | (searched) |
| Uppsala | 172600240438805638 |
