# Botkyrka FULL DEEP DIVE Round 4 — FINAL Report
**Date:** 2026-06-23
**Municipality:** Botkyrka (municipalityId: 172600240447194249)

## 🎯 Summary

| Metric | Value |
|---|---|
| **Live events BEFORE** | **32** |
| **Live events AFTER** | **36** |
| **Net new events published** | **+4** |

## 📊 4 NEW Botkyrka events published

### Barnteater i Hågelbyparken (3)
1. **Barnteater Nassim flippar UR! på semestern** — 15 juli kl 13 Hågelbyparken (fri entré)
2. **Barnteater Kom och sjung med Pippi Långstrump** — 22 juli kl 13 Hågelbyparken (fri entré)
3. **Barnteater Zillah och Totte** — 29 juli kl 13 Hågelbyparken (fri entré)

### Vatten & sport (1)
4. **Prova på vattenskidor gratis vid Lida Vattenskidklubb** — 4 juli 10-15 (SVWF + Lida Vattenskidklubb, all utrustning lånas, nybörjare alla åldrar)

## 📋 Sources processed

| # | Source | Result |
|---|---|---|
| 1 | hagelby.se/kalender | **3 NEW** barnteater julidatum (15, 22, 29 juli) |
| 2 | lida.se/evenemang | **1 NEW** Prova på vattenskidor 4 juli |
| 3 | botkyrka.se sommarguide | 0 NEW (Hågelby + Subtopia + Tumba bruksmuseum + Cirkus Cirkör + Botkyrka konsthall all already in live) |
| 4 | upplevbotkyrka.se | Already covered (Hågelby + Lida + Subtopia) |
| 5 | barnistan.se Botkyrka | Already covered |
| 6 | Web search | Found juli barnteater + simskola (latter not confirmed) |

## ✅ Rules compliance

| Rule | Result |
|---|---|
| municipalityId Botkyrka 172600240447194249 not null | ✅ ALL 4 |
| Image present (Hågelby source image + Lida source image) | ✅ ALL 4 |
| Push OFF (shouldNotifyUsers: false) | ✅ ALL 4 |
| Title dup check against 32 live | ✅ Multiple DUPs skipped (Klapphage, Bakluckeloppis, This is Botkyrka, Danskvällar, Barnteater Gräs, Sommarlov Hågelby) |
| Multi-date bundled | ✅ All 4 single-date events |
| Active/upcoming only (today 2026-06-23+) | ✅ ALL 4 |
| Clean prose descriptions, source-accurate | ✅ ALL 4 |
| ctaLink to source page | ✅ ALL 4 |
| Web search performed | ✅ |

## Skipped (DUP with live or past)
- Klapphage Hågelby 4H-gård (DUP)
- Bakluckeloppis (DUP)
- Barnteater Gräs (DUP — June)
- This is Botkyrka familjefestival (DUP)
- Danskvällar Hågelbyparkens dansgolv (DUP)
- Sommarlov i Hågelbyparken (DUP umbrella)
- Ateljé BK / Sommar i konstverkstan / Eric Magassa (DUPs)
- Therian-mask / Skulpturworkshop / Dans Subtopia (DUPs)
- Cirkus 7-14 Cirkus Cirkör (DUP)
- Tumba bruksmuseum handpapper / spargris swish (DUPs)
- Ekorrstigen / Skrävstastigen (DUPs)
- Folk Lab Verkstaden / Game on Hallunda (DUPs)
- Nationaldagen 6 juni (past)
- Getyoga 7 juni (past)
- Danskväll Highlights 11 juni (past)
- 10-årsjubileum Fire On Line 13 juni (past)
- Midsommarafton 19 juni (past)
- Utomhusyoga / Spela boule Korpen (adult/vuxen)
- Guidning blomflor (adult-focused)

## Sources

- [hagelby.se kalender](https://hagelby.se/kalender/)
- [lida.se evenemang](https://lida.se/evenemang/)
- [botkyrka.se sommarguide](https://www.botkyrka.se/uppleva-och-gora/botkyrkas-stora-sommarguide)
- [upplevbotkyrka.se kalendarium](https://www.upplevbotkyrka.se/kalendarium/)
- [barnistan.se Botkyrka/Salem/Tumba](https://www.barnistan.se/omrade/aktiviteter-barn-botkyrka/)
