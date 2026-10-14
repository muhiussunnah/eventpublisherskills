# Age Classification Audit — 844 Live Events
**Date:** 2026-05-21
**Scope:** All upcoming + ongoing events on FamMap dashboard
**Scanner:** Swedish-parent-aware classifier (v3 FINAL rules + new "hela familjen" rule)

## Summary

- **844 events scanned** with full descriptions
- **779 events** already correctly tagged ✅
- **65 events** need re-classification

## Confidence distribution

| Confidence | Count | Auto-apply? |
|---|---|---|
| High | 20 | Yes — clear pattern matches |
| Medium | 39 | Review — mostly "hela familjen → 0,18" |
| Low | 6 | Manual judgment needed |

---

## Group A: HIGH confidence (20) — apply directly

These match explicit description patterns: "från X år", "X-Y år", "X-Y åringar".

| # | Title | Current | Proposed | Rule |
|---|---|---|---|---|
| 11 | Lördagsbibblan: Bibblan pärlar! | 3,12 | 3,18 | från 3 år |
| 12 | Barnteater: Clownkalaset | 3,12 | 3,18 | från 3 år |
| 13 | Första Steget Miniakrobatik 2–7 år | 2,4 | 5,7 | range 5–7 år (likely mis-parsed; title says 2–7) |
| 14 | Sagolördag på Ekerö bibliotek | 3,12 | 3,18 | från 3 år |
| 15 | Sommarboken — läsutmaning Salem | 0,5 | 6,15 | range 6–15 år (conflicting with 0,5 earlier) |
| 20 | Monsterklubben — konst för barn | 6,12 | 6,18 | från 6 år |
| 22 | Workshop i modellera | 6,12 | 6,18 | från 6 år |
| 23 | Morsdagslunch på Sigtunastiftelsen | 0,2 | 3,12 | range 3–12 år (conflicting earlier) |
| 34 | Familjevisning på Södertälje konsthall | 5,12 | 5,18 | från 5 år |
| 47 | Knatteridning | 3,12 | 3,18 | från 3 år |
| 48 | Verkstad varje lördag | 4,12 | 4,18 | från 4 år |
| 49 | Sagostund med språk-lek | 2,6 | 2,18 | från 2 år |
| 52 | Sagor i parken | 3,12 | 3,18 | från 3 år |
| 54 | Sagoyoga | 4,12 | 4,18 | från 4 år |
| 58 | Stadsvandring med Christopher O'Regan | 10,18 | 0,14 | range 0–14 år (REJECT — already corrected by parent judgment) |
| 59 | Efter föris. Sagostund från 3 år | 3,12 | 3,18 | från 3 år |
| 60 | Sagostund på Märsta bibliotek | 3,12 | 3,18 | från 3 år |
| 61 | Sagostund på arabiska | 3,12 | 3,18 | från 3 år |
| 62 | Sagan om den lilla farbrorn | 3,12 | 3,18 | från 3 år |
| 65 | (truncated) | 3,12 | 3,18 | från 3 år |

**Notes:**
- #13, #15, #23 may be classifier picking secondary patterns — need manual review.
- #58 Stadsvandring should KEEP 10,18 (parent judgment overrides desc).

---

## Group B: MEDIUM confidence (39) — "hela familjen / family event → 0,18"

These are events tagged adult-only (18,18) or narrow ranges that contain "hela familjen", "familjedag", etc.

| # | Title | Current | Proposed |
|---|---|---|---|
| 1 | Sollentuna Rytmikkör Vårkonsert | 18,18 | 0,18 |
| 2 | Offerkälla vid Landsnora (nighttime full moon) | 18,18 | 0,18 (REVIEW — might be adult mystical) |
| 4 | Återbruksdagen 2026 | 18,18 | 0,18 |
| 5 | Fira nationaldagen med oss! | 3,12 | 0,18 |
| 6 | Kulturskolans dag | 6,15 | 0,18 |
| 7 | Prova Swimrun i Rösjön | 18,18 | 0,18 |
| 8 | Albydagen | 1,8 | 0,18 |
| 9 | Pusselkampen för hela familjen | 8,18 | 0,18 |
| 10 | Allemanut i Rimbo | 18,18 | 0,18 |
| 16 | Sommarkonsert med Salems kyrkokör | 18,18 | 0,18 |
| 17 | Vårkonsert med Salems stråkorkester | 18,18 | 0,18 |
| 21 | Emil i Lönneberga — teater för hela familjen | 4,12 | 0,18 |
| 24 | Sagostund i Sigtunastiftelsens bibliotek | 3,6 | 0,18 (might be wrong; sagostund is specific) |
| 25 | Plymmakarens vårparad på Skoklosters slott | 18,18 | 0,18 |
| 28 | Nationaldagen och Nykvarnsdagen 2026 | 18,18 | 0,18 |
| 29 | Kyrkornas Second Hand på Färingsö | 18,18 | 0,18 |
| 30 | Naturvandringar med Friluftsfrämjandet | 18,18 | 0,18 |
| 31 | SON OF ASSYRIA | 18,18 | 0,18 (REVIEW — unclear) |
| 32 | Båttur Södertälje till Riddarholmen | 18,18 | 0,18 |
| 33 | Till Havet | 18,18 | 0,18 |
| 35 | Konsert: El Sistema Södertälje | 18,18 | 0,18 |
| 39 | Familjelördag | 3,10 | 0,18 |
| 40 | Familjesöndag | 13,18 | 0,18 |
| 41 | Bakluckeloppis på Åkerby Gård | 18,18 | 0,18 |
| 42 | Mors Dag på Brasserie Vidbynäs | 18,18 | 0,18 (REVIEW — fancy restaurant lunch?) |
| 43 | Körkonsert i Nykvarns kyrka | 18,18 | 0,18 |
| 44 | INNER CHILD: Playing with Design | 18,18 | 0,18 (REVIEW — art exhibition) |
| 45 | MUCHA – Beyond Art Nouveau | 18,18 | 0,18 (REVIEW — immersive art) |
| 46 | Dukat till fest! Porslinsriket 200 år | 18,18 | 0,18 (REVIEW — porcelain museum) |
| 55 | Familjefredag | 1,8 | 0,18 |
| 57 | Kom stora kom små | 3,10 | 0,18 |
| 64 | Försommarmusik vid Görvälns slott | 18,18 | 0,18 |

**Fritidsgård fixes (medium confidence):**
| # | Title | Current | Proposed |
|---|---|---|---|
| 18 | Bokklubb på fritidsgården | 18,18 | 10,16 |
| 19 | Anpassad fritidsgård | 13,18 | 10,16 |
| 26 | Måndagskul på Ungdomens hus | 0,18 | 10,16 |
| 27 | Öppen sporthall (13–19 år) | 13,18 | 10,16 (REJECT — title states 13-19) |
| 50 | Läxhjälp | 7,16 | 10,16 |
| 53 | Kulturskolefestival | 6,15 | 10,16 (REJECT — culture school is broader) |

**Småbarn pattern:**
| # | Title | Current | Proposed |
|---|---|---|---|
| 38 | Barnbokprat på Öppna förskolan Kulan! | 1,5 | 1,4 |

---

## Group C: LOW confidence (6) — manual judgment

| # | Title | Current | Proposed | Notes |
|---|---|---|---|---|
| 3 | Efterhäng Unicornix | 18,18 | 3,5 | After-preschool unicorn show — 3,5 plausible |
| 36 | Efterhäng: Lamine Cissokho | 18,18 | 3,5 | After-preschool music — 3,5 plausible |
| 37 | Förskolans dag 2026: Sagan om skogen! | 1,8 | 3,5 | Preschool day — could be 1,5 or 3,5 |
| 51 | After föris | 1,8 | 3,5 | "After preschool" — 3,5 |
| 56 | Bokbio | 1,8 | 3,5 | Book cinema — could be wider |
| 63 | After föris | 3,10 | 3,5 | "After preschool" event |

---

## Apply plan

**Safe to auto-apply (~50 events):** all "hela familjen" → 0,18 where title clearly says family event, all "från X år" patches, all fritidsgård fixes.

**Review/reject (~15 events):** Stadsvandring (keep 10,18 per parent judgment), Öppen sporthall (keep 13,18 per stated), Kulturskolefestival, art exhibitions (Mucha, Inner Child, Porslin — likely adult content), Offerkälla full-moon (adult mystical), Mors Dag restaurant (adult).

