# RULE LEARNING — childMaxAge=18 for all-ages venues
**Date:** 2026-06-29
**Trigger:** Client complaint about "Max 17 år" showing on Storvretsbadet bathing event

## The Rule
**For all-ages events (bath/park/café/festival/exhibition/concert/opera/hike/farm shop):**
- ✅ childMinAge: 0 (or age recommendation), childMaxAge: **18**
- ❌ NEVER childMaxAge: 17 (the app displays "Max 17 år" which makes it look child-only)

**For kids-only events (sport camps/specific kid workshops/small kids storytime/bounce houses/lekplats):**
- ✅ childMaxAge: 17 (or younger) is correct

## Decision matrix

| Event type | childMin | childMax | Reason |
|---|---|---|---|
| Badplats / strand / simhall | 0 | **18** | Adults bath too |
| Slottspark / naturreservat / vandring | 0 (or age rec) | **18** | All ages walk |
| Festival / fest | 0 | **18** | All ages attend |
| Café / mötesplats / hembygdsgård | 0 | **18** | All ages |
| Utställning / museum / ateljé | 0 (or age rec) | **18** | All ages visit |
| Opera / teater / sommarteater | age rec | **18** | Adults attend |
| Konsert / sommarkonsert | 0 | **18** | All ages |
| Gårdsbutik / farm shop | 0 | **18** | All ages |
| Hamn / aktivitet (bowling etc) | 5+ | **18** | All ages |
| Spontanidrott (basket etc) | age rec | **18** | All ages |
| **Kids sport camp (fotboll/taekwondo/cirkus)** | 6+ | **17** | Kids only |
| **Kids workshop (graffiti/art camp)** | 8+ | **17** | Kids only |
| **Small kids storytime (sagoläsning/bilderboksmorgon)** | 0-3 | **6-8** | Small kids |
| **Lekplats / parklek / hoppborg** | 0-3 | **10-14** | Kids primary |
| **Simskola (swim school)** | 5-6 | **9-12** | Specific kids |

## Fixed this round (27 events)
**Storvretsbadet** — also got Mediterranean image swapped to Nordic indoor pool
**6 first-batch:** Sommarkonsert Tumba, Vi är Botkyrka festival, CentrumChill, Sommarkyrkan Sätra äng, Träffpunkt Enebyberg, Ekerö badhuset (0-17→0-18)
**10 venue-batch:** Lilla Värtan, Djursholms slottspark, Nora strand, Germaniaviken, Edsviken, Drottningholms slottspark, Lovö Prästgård, Södran badplats, Adelsö badplats, Lundhagen badplats (0-12 or 0-14 → 0-18)
**10 cultural-batch:** Spontanidrott basket, Operaafton Djursholms slott, Poppea opera, Eldgarnsö, Evert Lundquist, Konstringen, Hilma af Klint, Jungfrusund O'Learys, Adelsöleden 16 km, Adelsö Friluftsteater (X-17 → X-18 keeping cMin)

## Future commitment
ALL future publishes must apply this rule BEFORE publishing — not after.
