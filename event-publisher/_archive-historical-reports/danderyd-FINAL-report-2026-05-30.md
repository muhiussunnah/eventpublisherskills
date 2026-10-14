# Danderyd Event Publishing — FINAL Report (DEEP DIVE + WEB SEARCH)
**Date:** 2026-05-30
**Municipality:** Danderyd (municipalityId: 172600240455582858)

## Summary (the numbers — after deep dive + web search)

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **12** |
| **Events AFTER this session** | **21** |
| **Net new events published this session** | **+9** |

## Sources processed

| # | Source | Status |
|---|---|---|
| 1 | danderyd.se/evenemang | ✅ All 5 events scanned. 3 family events published |
| 2 | bibliotek.danderyd.se Arena (paginated 4+ pages, 60+ events) | ✅ 4 family-friendly with unique images published |
| 3 | svenskakyrkan kalender Danderyd | ⚠️ Parish URLs all 404 |
| BONUS Web Search | Parkteatern Kvarnparken + Ungdomscentrum Loppis + Sommarlov Danderyd | ✅ 2 more events published |

## 9 new events published this session

### From danderyd.se Source 1 (3)
1. Festlig lördag för alla – sång, pyssel och framtidsvisioner! (30 maj 10-16)
2. Fotoutställning med Danderyds fotoklubb (3-12 juni, 10-date bundle)
3. Nationaldagen 2026 vid Djursholms slott (6 juni 16:30-18)

### From bibliotek.danderyd.se Source 2 (4)
4. Sommarlovsboken på Danderyds bibliotek (30 maj - 29 aug)
5. Elevutställning - Oljemålningar & kolteckningar (Djursholms bibliotek, 5 dates)
6. Utställning – Historiska bilder (Enebybergs bibliotek, 7 dates)
7. Kreativ workshop på Stocksunds bibliotek (3 juni)

### From Web Search bonus venues (2)
8. **Parkteatern på Kvarnparken – familjeföreställning i Danderyd** (24 juni 10:30 + 13:00, multi-date bundle, ages 3-9, fri entré)
9. **Loppis på Ungdomscentrum & Seniorcentrum i Enebyberg** (16 juni 15-18 på Cedervägen 2)

## Image-duplicate audit + fix

During Loppis publish, accidental image collision detected with Festlig lördag (brush-1317900). **Immediately PATCH'd** Loppis to use unique Cedergrenska Tornet og:image (134KB) from Ungdomscentrum page. All 9 events now have unique images.

## Multi-date events bundled

- Fotoutställning: 10 dates
- Sommarlovsboken: spans 92 days
- Elevutställning: 5 dates
- Historiska bilder: 7 dates
- Parkteatern Kvarnparken: 2 dates (10:30 + 13:00 same day)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582858 (not null) | ✅ ALL 9 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 9 |
| Title duplicate check before publish | ✅ ALL 9 cleared |
| Source images (Rule #10.5) | ✅ ALL 9 |
| No duplicate images | ✅ ALL 9 (1 collision detected → PATCH'd to unique) |
| Active/upcoming dates only ≥ 2026-05-30 | ✅ ALL 9 |
| Multi-date bundled as single event | ✅ 5 bundles |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 9 |
| Filename campaign.jpg-{ts} | ✅ ALL 9 |
| Clean descriptions | ✅ ALL 9 |
| ctaLink to source page | ✅ ALL 9 |
| Per Rule #10.6 in-depth + web search | ✅ |

## Skipped (rule-compliant)

- Föräldravandring VT26 (existing), Konsert Monicas (existing), Seniorcenter invigning (senior), Bokcirkel Den stora utställningen (FULLBOKAD), Bokcirkel Farväl till Panic Beach/Den smala lyckan/Judarnas historia (adult-only), Texter & toner Idala (senior), Animation workshop / Digital teckning (existing baseline), Summerdays 2026 (existing)

## Web search sources used

- [Sommarlov 2026 – Danderyds kommun](https://sync.danderyd.se/uppleva-och-gora/sommarlov/)
- [Parkteatern – Kulturhuset Stadsteatern](https://kulturhusetstadsteatern.se/parkteatern)
- [Parkteatern Våra spelplatser](https://kulturhusetstadsteatern.se/parkteatern/vara-spelplatser)
- [Ungdomscentrum Danderyd](https://www.danderyd.se/ovriga-verksamheter/ungtfokus/ung-traffpunkt/om-ungdomscentrum/)
- [Danderyds kalender (kalender.se)](https://kalender.se/danderyd) — empty for current month

## Coverage assessment

Danderyd now at **+9 net new (21 total live)**. 2 spreadsheet sources + 1 web search bonus processed in-depth. Source 3 (svenskakyrkan) blocked by 404s on parish URLs. Bibliotek Arena gave unique per-event images. Web search surfaced Parkteatern Kvarnparken visit (24 juni) which was missing from danderyd.se kommun calendar — high-value family find.

Coverage now considered FULL per Rule #10.6 for accessible Danderyd family events.

Sources:
- [Sommarlov 2026 – Danderyds kommun](https://sync.danderyd.se/uppleva-och-gora/sommarlov/)
- [Parkteatern – Kulturhuset Stadsteatern](https://kulturhusetstadsteatern.se/parkteatern)
- [Parkteatern Våra spelplatser](https://kulturhusetstadsteatern.se/parkteatern/vara-spelplatser)
- [Ungdomscentrum Danderyd](https://www.danderyd.se/ovriga-verksamheter/ungtfokus/ung-traffpunkt/om-ungdomscentrum/)
