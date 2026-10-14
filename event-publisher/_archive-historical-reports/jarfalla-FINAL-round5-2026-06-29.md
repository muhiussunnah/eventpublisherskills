# Järfälla FULL DEEP DIVE Round 5 — FINAL Report (Updated)
**Date:** 2026-06-29
**Municipality:** Järfälla (municipalityId: 172600240455582862)

## Summary
- Live BEFORE: **15**
- Live AFTER: **27**
- Net NEW: **+12 events**

## 12 NEW Järfälla events published

### Source 1 + web: Festival + lekpark (2)
1. Järfällafestivalen 5 september Riddarparken Jakobsberg (kids 0-18)
2. Ålstaparken lekpark med flygledare-tema (kids 3-12)

### Web: Natur + slott + friluftsgård (3)
3. Görvälns naturreservat med Görvälnsbadet och Kallhällsbadet (kids 0-18)
4. Ängsjö friluftsgård med tipiby linbana äventyrsstig (kids 2-14)
5. Görvälns slott historiskt slott vid Mälaren (kids 3-18)

### Web: Dagläger + kulturskola + simhall (3)
6. Dagläger på Bas Barkarby 10-12 år (kids 10-12)
7. Järfälla kulturskola lovkurser och specialkurser (kids 5-17)
8. Järfällabadet simhall för familj (kids 0-18)

### Web round 2: Natur + bad + musik + kultur (4)
9. Västra Järvafältet naturreservat med Säbysjön fågelskådning (kids 4-18)
10. Bonäsbadet liten sandstrand med brygga och kiosk (kids 0-14)
11. Järfälla Musikkår blåsmusik konsert i Regementsparken (kids 0-18)
12. Kulturstigar i Kallhäll-Stäket 4 stigar historia (kids 6-18)

## Sources processed

| # | Source | NEW |
|---|---|---|
| 1 | jarfalla.se evenemang | 1 (Järfällafestivalen) |
| 2 | upplevjarfalla.se | 0 (covered) |
| 3 | bibliotek.jarfalla.se | 0 |
| 4 | evenemang.se | 0 (Cloudflare) |
| 5+6 | facebook.com | 0 (auth wall) |
| 7 | svenskakyrkan.se | 0 |
| 8 | ticketmaster.se | 0 (Round 4) |
| Web | Görvälns natur + slott + Ängsjö | 3 |
| Web | Ålstaparken | 1 |
| Web | Bas Barkarby + kulturskola + Järfällabadet | 3 |
| Web | Västra Järvafältet + Bonäsbadet + Musikkår + Kulturstigar | 4 |
| **Total** | | **12** |

## Rules compliance (ALL 12 events)

| Rule | Result |
|---|---|
| municipalityId Järfälla 172600240455582862 not null | ALL 12 |
| Image present (unique Unsplash) | ALL 12 |
| No duplicate images | ALL 12 |
| Push OFF | ALL 12 |
| Title dup-check vs 15 existing | ALL 12 |
| Multi-date bundled | YES where needed |
| Active/upcoming only | ALL 12 |
| Clean prose descriptions | ALL 12 |
| ctaLink to source page | ALL 12 |
| **childMaxAge=18 for all-ages venues** | ✓ (rule applied) |
| Status 200 OK | ALL 12 |

## Skipped per rules
- Demokratidagarna — adult focused
- Kallhäll 4H-gård — DUP existing
- Görvälns 4H-klubb — DUP existing
- Huset på Höjden — DUP existing
- Pop up bibliotek Riddarparken — DUP existing
- Skapandemåndag — DUP existing
- Kallhällsbadet — covered in Görvälns naturreservat description
- Ängsjöbadet — covered in Ängsjö friluftsgård description

## Final count
**27 live Järfälla events** (was 15, +12 NEW)

Sources:
- [jarfalla.se evenemang](https://www.jarfalla.se/fritidochkultur/kulturochnojen/evenemang.4.1ff597cb14c5be0c0e82f07c.html)
- [Järfällafestivalen 2026](https://www.jarfalla.se/fritidochkultur/kulturochnojen/jarfallafestivalen2026.4.3f3e90c8188b3c4768836ca.html)
- [Görvälns naturreservat](https://www.naturkartan.se/sv/jarfalla/gorvaln-2)
- [Görvälns slott](https://www.naturkartan.se/sv/stockholms-lan/gorvalns-slott)
- [Ängsjö friluftsgård](https://www.jarfalla.se/fritidochkultur/idrottochmotion/angsjofriluftsomrade.4.7649a918158917b879e26b0.html)
- [Järfälla kulturskolan](https://www.jarfalla.se/fritidochkultur/barnochunga/kulturskolan.4.640dac6b1300db73e7c80004945.html)
- [Järfälla simhall](https://www.jarfalla.se/fritidochkultur/idrottochmotion/simhall.4.640dac6b1300db73e7c800013908.html)
- [Västra Järvafältet](https://www.lansstyrelsen.se/stockholm/besoksmal/naturreservat/vastra-jarvafaltet.html)
- [Järfälla badplatser](https://www.jarfalla.se/fritidochkultur/idrottochmotion/badplatser.4.640dac6b1300db73e7c800015282.html)
- [Järfälla Musikkår](https://www.jarfallamusikkar.se/konsertkalender/)
- [Kulturstigar Kallhäll-Stäket](https://stockholmslansmuseum.se/besoksmal/kulturstigar-i-kallhall-staket/)
- [Upplev Järfälla](https://upplevjarfalla.se/lovaktiviteter)
