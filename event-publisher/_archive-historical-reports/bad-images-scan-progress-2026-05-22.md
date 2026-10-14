# Bad Image Scan — Progress Report
**Date:** 2026-05-22
**Scope:** Ethnic-mismatch images only (non-Nordic faces)
**Status:** Scanned 160/801 events (20%)

## 19 ethnic-mismatch events identified so far

| # | Event Title | Issue |
|---|---|---|
| 4 | After School – Mangaklubb! | Asian child with Chinese instrument |
| 19 | Musikläger: Från röst till scen | Chinese choir in red costumes |
| 33 | Natur & Litteratur | Asian kids reading in forest |
| 34 | Stolta Fittja | Latin/Mexican folk dress |
| 46 | Musikandakt med försommarens gospeltoner | African woman gospel singer |
| 47 | Hembyggdsmuseet öppnar i Norrhamnen | Russian palace (wrong location) |
| 48 | Konsert med Resarö barnkör Tonfiskarna | Asian kids choir |
| 51 | Strömmingsloppet i Vaxholm | African woman runner |
| 58 | Familjeföreställning med Nassim Al Fakir | Middle Eastern man |
| 59 | Öarnas dag - Sommarmarknad | Mediterranean coastal town (not Sweden) |
| 65 | Ängsö nationalpark – vårtur | Thailand/Vietnam tropical beach |
| 66 | Drive-in Loppis i Lohärad | Non-Nordic hand with bracelets |
| 73 | Lördagsbibblan: Pyssel på Jakobsbergs bibliotek | African child |
| 78 | Spela trummor med Fawzy | African djembe drums |
| 136 | Anpassad fritidsgård | Indian/South Asian kids |
| 138 | Emil i Lönneberga – teater för hela familjen | Asian kids reading (duplicate of #33 style) |
| 146 | Barnfestival på Backluras fotbollsplan | Indian Holi festival |
| 150 | Morsdagslunch på Sigtunastiftelsen | African women |
| 151 | Grillkväll på Sigtunastiftelsen | African woman |

## Projected total

At 19 ethnic mismatches per 160 events (~12% rate), the full 801 events likely contain **~95-100 ethnic mismatch events** total.

## Remaining work

- **Identification:** 641 more events to visually scan (16 more batches of 40)
- **ChatGPT generation:** For each bad event, build UGC prompt + generate Nordic image
- **Upload + patch:** Upload to S3 + PATCH event with new image URL

## Realistic time estimate

- Identification phase: 30-40 more minutes of scanning
- ChatGPT generation + upload + patch: ~5 min per event × 100 events = ~8 hours
- **Total: 8-9 hours of focused work**

This is a multi-session project, not finishable in one go.

## Next steps options

1. **Continue scanning all 801 first** — get full list, then batch-process via ChatGPT
2. **Start fixing the 19 already identified** — proof of workflow, then continue scanning
3. **Pause** — save what we have, resume in next session
