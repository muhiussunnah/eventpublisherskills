# Botkyrka Event Publishing — Progress
**Date:** 2026-05-30
**Municipality:** Botkyrka (municipalityId: 172600240447194249)

## Source 1 status (botkyrka.se/evenemangsarkiv)

| Step | Result |
|---|---|
| Total events scraped from source 1 | **336** |
| After dedupe + skip senior/inställt | 16 unique titles |
| Family-friendly with usable og:image | 3 |
| Published this batch | **+3** |

### Published from Source 1

1. **Upptäck utställningen Från spargris till Swish** (Tumba bruksmuseum, 7 juni 2026) — museum exhibition for kids + adults about money history. Source image: TBM_Lyckoslanten photo (93KB).
2. **Bottenstädning vid Slagstabadet** (8 juni 2026) — community cleanup at Slagsta swimming spot with divers. Source image: dyk2.jpg (176KB).
3. **Upptäck Botkyrka - Visning av Hågelbyparkens underbara trädgård** (10 juni 2026) — guided garden tour at Hågelbyparken. Source image: Hågelby park photo (53KB).

### Skipped from Source 1 (no real image / not family-friendly)

- Kompis Sverige mötesplats Alby — only Botkyrka logo as og:image (no real photo)
- Läxhjälp på Tumba bibliotek — only logo image
- Folk Lab Odling/Verkstaden — only logo image
- Appoteket på Tumba bibliotek — only logo image
- Zumba Guld Tullinge — senior class
- Zumba Fitness Tullinge — adult class
- Mötesplats funktionsnedsättningar — adult/special needs (and was in existing)
- Författarsamtal uzbekiska — already in existing baseline
- Folk Lab Entreprenörskap — adult business workshop
- Arbetsmarknads- och vuxenutbildningsnämnden sammanträder — municipal council meeting (adult-only)
- Föreläsning Brit Stakston — adult lecture on fake news

## Rules verified for the 3 published

| Rule | Result |
|---|---|
| municipalityId set (172600240447194249) | ✅ ALL 3 |
| shouldNotifyUsers: false | ✅ ALL 3 |
| Title duplicate check before publish | ✅ ALL 3 cleared |
| Source image used (Rule #10.5 source-first) | ✅ ALL 3 from botkyrka.se CDN |
| No duplicate images | ✅ Unique per event |
| Active/upcoming dates only (≥ 2026-05-30) | ✅ ALL 3 (7, 8, 10 juni 2026) |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 3 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 3 |
| Description clean, no JS/code pollution | ✅ ALL 3 |
| ctaLink to source page | ✅ ALL 3 |

## Botkyrka counts

| Status | Count |
|---|---|
| Before this session | 43 |
| After Source 1 batch | **46** |
| Net new | +3 |

## Remaining sources (still to process)

| # | Source |
|---|---|
| 2 | bibliotek.botkyrka.se/evenemang |
| 3 | evenemang.se/se/stockholms-län/botkyrka |
| 4 | tickster.com/.../botkyrka-rtf |
| 5 | facebook.com/botkyrka/events |
| 6 | svenskakyrkan.se/botkyrka/kalender |
| 7 | ticketmaster.se/search?q=Botkyrka |

## State preserved

- `__botkyrka_events` (336 URLs) in localStorage on botkyrka.se tab
- `__botkyrka_publishable` (16 candidates) in localStorage
- `__botkyrka_details` (9 fetched details) in localStorage
- `window.__cityMunId`, `window.__cityPlaces`, `window.__publishBotkyrka` on dashboard tab

Ready to continue with Source 2 (bibliotek.botkyrka.se) next.
