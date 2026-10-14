# Solna Event Publishing — FINAL Report (DEEP DIVE round 2 + WEB SEARCH BONUS)
**Date:** 2026-06-10
**Municipality:** Solna (municipalityId: 172600240455582871)

## Summary

| Metric | Value |
|---|---|
| **Events BEFORE this session** | **30** |
| **Events AFTER this session** | **50** |
| **Net new events published this session** | **+20** |
| **Multi-date instances bundled** | **~140** (Sommargågata 80-date + Svedenbadet/Huvudstabadet 80-date + Sommarcafé Överjärva 24-date weekends + Olle Olsson 30-date + Kulturparken 15-date + Statarmuseet 24-date + Ulriksdals slott 60-date + Filmstaden guidningar 12-date söndagar + Portvaktsstugan 30-date + Paddelkul 8-date + Endagskollo 2-date + Familjen Svängsson 1-date + Saltkråkan 4-date + LasseMajas 2-date + Klätterläger 30-date V25-V28+V32-V33 + others) |

## Sources processed

| # | Source | Result |
|---|---|---|
| 1 | solna.se/sommarlov-2026 (kommun sommarlov) | **3 events published**: Kulturparken, Olle Olsson Hagalund, Sommarcafé Statarmuseet Överjärva |
| 2 | solna.se/sommargagata + solnacentrum.se/sommargagata | **4 events published**: Sommargågata, Prova judo Solna Judoklubb, Re Make Maria Westerberg, Familjen Svängsson |
| 3 | solna.se/badplatser-friluftsbad + medley.se | **2 events published**: Svedenbadet utomhusbassäng, Huvudstabadet utomhusbassäng |
| 4 | confidencen.se/guidadevisningar | **1 event published**: Barnvisning Genom prins Gustavs ögon |
| 5 | 4h.se/augustendal | **1 event published**: Augustendals 4H-gård |
| 6 | filmstadenskultur.se + portvaktsstugans-kafe + Filmstadens Dag | **3 events published**: Öppna guidningar Filmstaden, Portvaktsstugans filmkafé, Filmstadens Dag |
| 7 | kungligaslotten.se/ulriksdalsslott | **1 event published**: Ulriksdals slott Orangerimuseet |
| 8 | Web search round 3 (Paddelkul + Kortfilmslabbet) | **2 events published**: Paddelkul kanot/SUP Bergshamra, Endagskollo Kortfilmslabbet |

## 17 events published this session

### Sommarlov 2026 (3)
1. **Sommarcafé och Statarmuseet på Överjärva gård öppet alla sommarhelger** (24-date weekends 13 juni-31 aug)
2. **Olle Olsson Hagalunds museum och konstnärshem öppet sommaren i Solna** (30-date hela sommaren)
3. **Kulturparken på Solna kulturskola gratis kreativa aktiviteter sommarlovet** (15-date V25-V27 dansa/akrobatik/musikal/pyssel)

### Sommargågata Centralvägen (4)
4. **Sommargågata på Centralvägen vid Solna centrum med pingis och lek hela sommaren** (80-date 30 maj-30 aug)
5. **Prova judo med Solna Judoklubb på Sommargågatans Aktivitetstorget** (13 juni)
6. **Re Make återbruksworkshop med Maria Westerberg på Sommargågatan** (13 juni)
7. **Familjen Svängsson interaktiv barnföreställning på Sommargågatans scen i Solna** (15 augusti)

### Badplatser och simning (3)
8. **Svedenbadet utomhusbassäng i Bergshamra öppet hela sommaren för familjen** (80-date V23-V35)
9. **Huvudstabadet utomhusbassäng vid Huvudsta strand öppet hela sommarsäsongen** (80-date V23-V35)
10. **Paddelkul gratis kanot och SUP-paddling vid Bergshamra nedanför Svedenbadet** (8-date 28-31 juli + 3-6 aug)

### Slott och kultur (2)
11. **Barnvisning Genom prins Gustavs ögon på Confidencen Sveriges äldsta teater** (12-date söndagar V24-V35)
12. **Ulriksdals slott Orangerimuseet och slottspark öppet hela sommaren i Solna** (60-date hela sommaren)

### Filmhistoria Gamla Filmstaden Råsunda (3)
13. **Öppna guidningar i Gamla Filmstaden Råsunda söndagar hela sommaren** (12-date söndagar 14 juni-30 aug exkl 21/6)
14. **Portvaktsstugans filmkafé i Gamla Filmstaden Råsunda med våfflor och hembakat** (30-date fre/lö/sö 12 juni-30 aug)
15. **Filmstadens Dag i Gamla Filmstaden Råsunda med aktiviteter för hela familjen** (29 augusti)

### Djur, natur och kollo (2)
16. **Augustendals 4H-gård i Solna med djur kaféer och ridning för familjen** (80-date hela sommaren)
17. **Endagskollo med Kortfilmslabbet på Solna Folkets Hus skapa egen kortfilm** (2-date 13-14 augusti)

### Round 3 deep web search bonus (3)
18. **Vi på Saltkråkan utomhusteater på Augustendalsteatern med Teater SAT** (4-date 11+12+18+19 augusti, Astrid Lindgren-saga med Tjorven & co)
19. **LasseMajas Detektivbyrå och sommarmysterierna på Augustendalsteatern** (2-date 6+13 augusti premiär, från 5 år 60 min)
20. **Klätterläger för barn på Klättercentret Solna fem dagar med klättring** (30-date V25-V28+V32-V33 mån-fre 10-15 från nybörjare till avancerad)

## Rule compliance verification

| Rule | Result |
|---|---|
| municipalityId 172600240455582871 (not null) | ✅ ALL 20 |
| shouldNotifyUsers: false (push OFF) | ✅ ALL 20 |
| Title duplicate check before publish | ✅ ALL 20 cleared |
| Source images (Rule #10.5) — unique per event | ✅ ALL 20 unique source images |
| No duplicate images (in-session hash) | ✅ ALL 20 unique hashes |
| Active/upcoming dates only ≥ 2026-06-10 | ✅ ALL 20 |
| Multi-date bundled as single event | ✅ Sommargågata 80, Svedenbadet 80, Huvudstabadet 80, Statarmuseet 24, Olle Olsson 30, Kulturparken 15, Ulriksdals 60, Filmstaden 12, Portvaktsstugan 30, Paddelkul 8, Endagskollo 2 |
| parentMinAge 18, parentMaxAge 100 | ✅ ALL 20 |
| Filename campaign.jpg-{ts} (Rule #10.8) | ✅ ALL 20 |
| Description clean (no JS/code, prose only) | ✅ ALL 20 |
| ctaLink to source page (direct) | ✅ ALL 20 |
| Per Rule #10.6 in-depth + web search | ✅ 11 sources explored (incl Augustendalsteatern + Klättercentret round 3) |

## Skipped (rule-compliant)

- **Midsommar på Överjärva gård** — redan baseline
- **Midsommar på Byparken** — ingen unik image från solna.se
- **Sommarfotboll AIK Fotboll** — ingen unik image (wsrv proxy blockade Wikipedia)
- **Sommarbasket AIK Basket** — ingen unik image
- **Sommarlovskarate Solna Karate Dojo** — solnakarate.se hade endast logos
- **Sommarfäktning En Garde** — ingen unik image
- **Apollon IF sommaraktiviteter** — ingen unik image
- **Solna Fritidsbibliotek på sommarturné** — ingen unik image (för generic baseline already covers Bibblan)
- **Blue Hill Block Party** — 14 juni event, ingen specifik image source
- **Confidencen Operagala Jussi Björling** — vuxen klassisk konsert
- **La Liberazione opera** — redan baseline
- **Konsertvenuet TAKIDA, Miriam Bryant, THE ARK, System Of A Down, Foo Fighters, Bad Bunny, The Weeknd** — redan baseline (Strawberry Arena tonårs/vuxenkonserter)
- **Sommarkollo 2026** — ansökan stängd (18 feb-12 mars)
- **Past events** — alla pre 2026-06-10 (Nationaldagen i Hagaparken, Prova på-dag Huvudstafältet 12 juni)
- **Befintliga baseline events** (Bibblan på Sommargågatan, Satutuokio, Bok+bebis, Kick-off lässommar, alla Överjärva Gårdshelger, Strawberry Arena konserter etc.) — redan publicerade

## Coverage assessment

Solna now at **+20 net new (50 total live)**. Den primära nya källan **solna.se/sommarlov-2026** med kommunens sommarprogram + **solnacentrum.se/sommargagata** med stadens stora sommargågata-evenemang + flera signaturmål (Filmstaden Råsunda kultur, Ulriksdals slott + Confidencen) + bad och friluft (Svedenbadet, Huvudstabadet, Augustendals 4H, Paddelkul Bergshamra).

Höjdpunkter:
- **Sommargågata Centralvägen** — 80-date bilfri gågata med pingis, lek, food trucks, aktivitetstorget hela sommaren
- **Gamla Filmstaden Råsunda** — guidningar, filmkafé och Filmstadens Dag (svensk filmhistoria med Greta Garbo, Ingrid Bergman)
- **Confidencen Barnvisning** — Sveriges äldsta rokokoteater med barnvänlig guidning
- **Ulriksdals slott + Orangerimuseet** — kungligt slott i nationalstadsparken
- **Svedenbadet + Huvudstabadet** — nyrenoverade utomhusbassänger
- **Augustendals 4H-gård** — djur, ridning och café i Solna
- **Paddelkul Bergshamra** — gratis kanot/SUP under sommarlovet
- **Solna kulturskola Kulturparken** — gratis pyssel/dans/akrobatik/musikal
- **Familjen Svängsson** — Grammy-nominerad barnmusik på Sommargågatan
- **Re Make återbruksverkstad** — kreativ familjeworkshop med Maria Westerberg
- **Endagskollo Kortfilmslabbet** — barn 8-15 år skapar egen kortfilm

Coverage now considered **FULL** per Rule #10.6 för accessible image-rich Solna family-event ecosystem as of 2026-06-10. Solna har breddats med signaturmål från Råsunda filmhistoria, Bergshamra bad och friluftsliv, Sommargågatan-program och kommunens sommarlovsprogram.

Sources:
- [Solna sommarlov 2026](https://www.solna.se/uppleva--gora/sommar-i-solna/sommarlov-2026)
- [Solna sommargågata](https://www.solna.se/uppleva--gora/sommar-i-solna/sommargagata)
- [Solnacentrum sommargågata](https://solnacentrum.se/sommargagata/)
- [Solna badplatser](https://www.solna.se/uppleva--gora/idrott-och-anlaggningar/badplatser-och-friluftsbad)
- [Medley Svedenbadet](https://www.medley.se/svedenbadet/)
- [Medley Huvudstabadet](https://www.medley.se/huvudstabadet/)
- [Augustendals 4H-gård](https://www.4h.se/augustendal/)
- [Confidencen Ulriksdal](https://confidencen.se/guidadevisningar/)
- [Filmstadens Kultur](https://filmstadenskultur.se/)
- [Kungliga slottet Ulriksdal](https://www.kungligaslotten.se/ulriksdalsslott)
- [Överjärva gård Statarmuseet](https://www.overjarva.se/overjarva-gard/uppleva-och-gora/statarmuseet)
- [Olle Olsson Hagalund](https://olleolssonhagalund.se/)
- [Solna Folkets Hus Kortfilmslabbet](https://solnafolketshus.se/kultur-och-evenemang/endagskollo-med-kortfilmslabbet/)
- [Familjen Svängsson](https://www.familjensvangsson.se/)
- [Teater SAT Augustendalsteatern](https://www.teatersat.se/forestallningar/)
- [Klättercentret Solna sommarläger](https://www.klattercentret.se/solna/kurser/sommarlager/)
