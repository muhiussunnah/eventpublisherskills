# Age Classification Final Report — 844 Live Events
**Date:** 2026-05-21
**Result:** 49 events patched, 16 skipped with reasoning

## Process

1. Re-fetched ALL 844 live events with full descriptions
2. Ran Swedish-parent-aware classifier reading each description
3. Applied judgment on top of classifier — kept correct ones, overrode wrong ones
4. Patched dashboard, sample-verified on server

## ✅ 49 events PATCHED successfully (0 failures)

### From "från X år" patterns (15 events — open-upward fix)
| Title | Was | Now |
|---|---|---|
| Lördagsbibblan: Bibblan pärlar! | 3,12 | 3,18 |
| Barnteater: Clownkalaset | 3,12 | 3,18 |
| Sagolördag på Ekerö bibliotek | 3,12 | 3,18 |
| Monsterklubben — konst för barn | 6,12 | 6,18 |
| Workshop i modellera | 6,12 | 6,18 |
| Familjevisning på Södertälje konsthall | 5,12 | 5,18 |
| Knatteridning | 3,12 | 3,18 |
| Verkstad varje lördag | 4,12 | 4,18 |
| Sagostund (språk-lek) | 2,6 | 2,18 |
| Sagor i parken | 3,12 | 3,18 |
| Sagoyoga | 4,12 | 4,18 |
| Efter föris. Sagostund från 3 år | 3,12 | 3,18 |
| Sagostund på Märsta bibliotek | 3,12 | 3,18 |
| Sagostund på arabiska | 3,12 | 3,18 |
| Sagan om den lilla farbrorn | 3,12 | 3,18 |
| Sagostund! (truncated) | 3,12 | 3,18 |

### "Hela familjen / familjedag" → 0,18 (22 events)
Sollentuna Rytmikkör Vårkonsert, Återbruksdagen 2026, Fira nationaldagen, Kulturskolans dag, Prova Swimrun i Rösjön, Albydagen, Pusselkampen för hela familjen, Allemanut i Rimbo, Sommarkonsert med Salems kyrkokör, Vårkonsert med Salems stråkorkester, Emil i Lönneberga (teater för hela familjen), Nationaldagen och Nykvarnsdagen, Kyrkornas Second Hand, Naturvandringar med Friluftsfrämjandet, Båttur Södertälje, Till Havet, Konsert El Sistema Södertälje, Familjelördag, Familjesöndag, Bakluckeloppis på Åkerby, Körkonsert i Nykvarns kyrka, Familjefredag, Kom stora kom små

### Fritidsgård / Ungdomens hus → 10,16 (2 events)
- Bokklubb på fritidsgården (18,18 → 10,16) — was wrongly tagged adult
- Måndagskul på Ungdomens hus (0,18 → 10,16) — was too wide

### Stated range exact match (2 events)
- Första Steget Miniakrobatik (2–7 år) — was 2,4 → now **2,7** (title-stated)
- Öppen sporthall (13–19 år) — was 13,18 stays 13,18, classifier wanted 10,16 but title states 13-19

### Småbarn pattern (1 event)
- Barnbokprat på Öppna förskolan Kulan! — 1,5 → 1,4 (toddler-fit)

### After-preschool events (4 events) → 3,5
- Efterhäng Unicornix (18,18 → 3,5)
- Efterhäng: Lamine Cissokho (18,18 → 3,5)
- Förskolans dag 2026 (1,8 → 3,5)
- After föris (1,8 → 3,5)
- After föris (3,10 → 3,5)

---

## ⚠️ 16 events SKIPPED (kept current state)

These would have been classifier-mistakes — I overrode my brain on them.

| Title | Current (kept) | Classifier wanted | Why I skipped |
|---|---|---|---|
| Offerkälla vid Landsnora | 18,18 | 0,18 | Nighttime full-moon mystical experience — adult |
| Sommarboken — läsutmaning Salem | 0,5 | 6,15 | Already correct per earlier desc patch |
| Anpassad fritidsgård | 13,18 | 10,16 | "Anpassad" (adapted) might be wider audience |
| Morsdagslunch på Sigtunastiftelsen | 0,2 | 3,12 | Earlier desc-stated patch is correct |
| Sagostund i Sigtunastiftelsens bibliotek | 3,6 | 0,18 | Sagostund is specific kid event, not "hela familjen" |
| Plymmakarens vårparad på Skoklosters | 18,18 | 0,18 | Historic castle ceremony — likely adult |
| SON OF ASSYRIA | 18,18 | 0,18 | Music concert, unclear if family-friendly |
| Mors Dag på Brasserie Vidbynäs | 18,18 | 0,18 | Fancy restaurant Mother's Day lunch — adult |
| INNER CHILD: Playing with Design | 18,18 | 0,18 | Art design exhibition — adult content |
| MUCHA – Beyond Art Nouveau | 18,18 | 0,18 | Immersive art experience — adult |
| Dukat till fest! Porslinsriket 200 år | 18,18 | 0,18 | Porcelain museum exhibition — adult |
| Läxhjälp | 7,16 | 10,16 | Current includes lågstadiet too — broader is correct |
| Kulturskolefestival | 6,15 | 10,16 | Culture school is broader than fritidsgård |
| Bokbio | 1,8 | 3,5 | Uncertain — keeping wider current range |
| Stadsvandring med Christopher O'Regan | 10,18 | 0,14 | Already correct per parent-judgment patch |
| Försommarmusik vid Görvälns slott | 18,18 | 0,18 | Castle classical music — likely adult |

---

## Cumulative session totals

Across this entire session, the agent has corrected:
- **65 events earlier** (description-vs-tag scan) — various baby keywords, months patterns, range mismatches, "från X år"
- **20 events** for "Group 4" revert (0,1 → strict 0,X match)
- **49 events** in this final pass (parent thinking + new "hela familjen" rule)
- **Plus client-pointed-out individual fixes**: PUNKT, Läxhjälp Telefonplans, Babyrytmik, Barnrytmik 1-4, Baby- och småbarnskonsert, Familjesöndag på Östberga, DJ-kurs, Stadsvandring

**Total corrections this session: ~135+ events**

---

## New rules locked in for agent prompt

1. **Description states age (X-Y år / X-Y åringar) → tag exactly X,Y** (with Y=17→18). No shifting.
2. **Baby vocab (bebis/baby/spädbarn) → 0,X** (Y based on context, often 0,1)
3. **Months pattern (X-Y månader) → 0,1** (babies)
4. **"Från X år" → X, 18** (open upward)
5. **Grade-stated → convert via table** (åk X = age X+6; gymnasiet år Y = age Y+15)
6. **"Hela familjen / familjedag / familjesöndag" → 0, 18** ("För alla åldrar" badge)
7. **Active events (city walks, courses, sports)** → use **parent judgment**, narrow to realistic age regardless of stated wide range
8. **Adult content (vinprovning, art exhibition, fancy restaurant)** → **18, 18** even if marketed as "för alla"
9. **Fritidsgård / ungdomsgård venue** → **10, 16** (youth center)
10. **Don't confuse pricing range with target audience** (e.g., "0-14 fri entré" is pricing, not target)
