# Södermanland (+ Knutsbol, Degerfors) — Permanent Places → Events — FINAL REPORT
**Date:** 2026-10-18
**Source:** `0915-Famies - Vad ska vi hitta pa idag.html` (embedded `places`, 1088 places). Compared with the app:
the only region not yet published was **Södermanland** (52 places). One Örebro-län place was also missing:
**Degerfors Hembygdsgård Knutsbol**.
**Flow per place:** duplicate check → Organizer → Venue → Event (POST /admin/organizations → /admin/places → /admin/events),
`shouldNotifyUsers: false` on every event.

## Result

| | Count |
|---|---|
| Södermanland places in the HTML | 52 |
| Already in the app (Parken Zoo, Nyköpingshus, Strängnäs domkyrka, Gripsholms slott) | 4 |
| + missing Örebro place (Knutsbol, Degerfors) | 1 |
| Candidates researched (7 parallel research agents, batches S1–S7) | 49 |
| **Published (organizer + venue + event)** | **40** |
| Skipped (reasons below) | 9 |
| Södermanland events live after the run | 44 (4 + 40) |

Organizers: 33 used — 31 new + reused **Medley** (Munktellbadet, Ramdalen) and **Nordiska museet** (Julita gård);
kommun organizers created once and shared (Eskilstuna ×4, Katrineholm ×4, Trosa, Nyköping, Strängnäs, Flen, Vingåker).

## Final audit (API re-fetch of all 40 events): 0 issues
- municipality set on every place (Eskilstuna, Gnesta, Strängnäs, Nyköping, Oxelösund, Trosa, Katrineholm, Vingåker, Flen)
- parent 18–100, childMaxAge 18 (childMinAge 2 Trosa Aktivitetspark, 6 Zero One Six, 8 Escape Room — real limits)
- `isRecurring` + recurrence on all; window open on every listed day; no event ends in the past
- 2 interests on all; ctaText "Läs mer" + official ctaLink; descriptions 391–567 chars, Swedish, official facts only
- 0 duplicate titles; 0 duplicate / near-duplicate images (dHash check + visual contact sheet of all 40)
- all images re-uploaded to fammap S3; 31 new organizers checked — 26 have the official logo as avatar; 5 small associations have no official logo (no avatar):
  Hälleforsnäs Gjuterimuseum, Hjälmargården, Åkers hembygdsförening, Mariefreds hembygdsförening, Ulvhälls hällar
- privacy: no personal-name emails or private phones (several were found and left out on purpose)

## Published (40)

| # | Venue | Kommun | Organizer | Recurrence | Event ID | Notes |
|---|---|---|---|---|---|---|
| 3 | Munktellmuseet | Eskilstuna | Munktellmuseet | Mon,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 475130593332463320 | org Munktellmuseet (Volvo CE); Mon-Sat 11-16 |
| 4 | Munktellbadet | Eskilstuna | Medley | Daily 09:00–18:00, 2026-09-01 → 2027-12-31 | 475130658964932422 | org Medley reused; family pool 9-18 window |
| 5 | Eskilstuna konstmuseum | Eskilstuna | Eskilstuna kommun | Wed,Thu,Fri,Sat,Sun 12:00–16:00, 2026-09-01 → 2027-12-31 | 475130963353962421 | org Eskilstuna kommun created (white logo on dark) |
| 6 | Eskilstuna stadsmuseum | Eskilstuna | Eskilstuna kommun | Wed,Thu,Fri,Sat,Sun 12:00–16:00, 2026-09-01 → 2027-12-31 | 475131030102115363 | org Eskilstuna kommun reused |
| 7 | Rademachersmedjorna | Eskilstuna | Eskilstuna kommun | Daily always open, 2026-09-01 → 2027-12-31 | 475131321564300434 | always open outdoor; leksmedja seasonal |
| 8 | Ebelingmuseet | Eskilstuna | Eskilstuna kommun | Wed,Thu,Fri,Sat,Sun 12:00–16:00, 2026-09-01 → 2027-12-31 | 475131389428139265 | postcode 644 32 from OSM |
| 9 | Leo's Lekland Eskilstuna | Eskilstuna | Leos Lekland Eskilstuna | Daily 10:00–19:00, 2026-09-01 → 2027-12-31 | 475125470434722851 | org per-location (convention); chain photo from official Eskilstuna page (volcano) |
| 11 | Escape Room Eskilstuna – Quezzle | Eskilstuna | Quezzle AB | Daily 10:00–22:00, 2026-09-01 → 2027-12-31 | 475125772114232466 | Quezzle; childMinAge 8 (8+ with adult, 14+ alone); only adult photo exists |
| 12 | Bowlers Eskilstuna | Eskilstuna | Bowlers Eskilstuna | Daily 12:00–20:00, 2026-09-01 → 2027-12-31 | 475125846110143746 | photos on official Eskilstuna site may be shot in Borås |
| 13 | Zero One Six Skatepark | Eskilstuna | KFUM Eskilstuna Skateboard, Inlines & BMX club | Daily 14:00–20:00, 2026-09-01 → 2027-12-31 | 475126209236206962 | membership required; childMinAge 6 |
| 44 | Museispårvägen Malmköping | Flen | Museispårvägen Malmköping AB | Sat,Sun 11:00–15:00, 2027-05-15 → 2027-08-29 | 475132612889838961 | 2027 copied 15 May-29 Aug weekends 11-15 |
| 45 | Sparreholms slotts bilmuseum | Flen | Sparreholms Slott AB | Tue,Wed,Thu,Fri,Sat,Sun 12:00–17:00, 2027-06-23 → 2027-08-09 | 475132708704519575 | only car museum public; 2027 copied 23 Jun-9 Aug Tue-Sun 12-17; phone omitted (owner unknown) |
| 46 | Hälleforsnäs Gjuterimuseum | Flen | Föreningen Hälleforsnäs Gjuterimuseum | Thu,Fri,Sat 11:00–15:00, 2026-09-01 → 2027-12-31 | 475133057637057968 | no org phone/logo (only named board members' mobiles) |
| 47 | Flens simhall | Flen | Flens kommun | Tue,Wed,Thu,Fri,Sat,Sun 12:00–15:30, 2026-09-01 → 2027-12-31 | 475133118035035630 | Monday lap-swim only excluded; window 12-15:30; summer hours unknown |
| 49 | Sagostigen | Flen | Sagostigen AB | Daily 10:00–16:00, 2027-05-14 → 2027-08-22 | 475133183977883149 | 2027 season officially announced 14 May-22 Aug |
| 51 | Skottvångs Grufva | Gnesta | Skottvångs Grufva AB | Tue,Wed,Thu,Fri,Sat,Sun 12:00–16:00, 2027-06-23 → 2027-08-16 | 475126275472655841 | 2027 copied from 2026 span 23 Jun-16 Aug Tue-Sun 12-16 |
| 35 | Julita gård | Katrineholm | Nordiska museet | Daily 10:00–17:00, 2027-06-15 → 2027-08-23 | 475122859195271092 | org Nordiska museet reused; 2027 copied 15 Jun-23 Aug |
| 36 | Katrineholms simhall | Katrineholm | Katrineholms kommun | Tue,Wed,Thu,Fri,Sat,Sun 08:30–16:00, 2026-09-01 → 2027-12-31 | 475137087792776793 | org Katrineholms kommun created; Tue-Sun 08:30-16 |
| 37 | Backavallen – Kronfågel isarena och Kronfågel ishall | Katrineholm | Katrineholms kommun | Mon,Tue,Wed 14:00–15:30, 2026-09-01 → 2027-04-04 | 475137306802554504 | fixed season schedule Mon-Wed 14-15:30 until 2027-04-04; fee not stated -> isFree false |
| 38 | Djulöområdet | Katrineholm | Katrineholms kommun | Daily always open, 2026-09-01 → 2027-12-31 | 475137421541934777 | always open area; venue contacts = Djulö Camping |
| 39 | Kulturhuset Ängeln | Katrineholm | Katrineholms kommun | Mon,Tue,Wed,Thu,Fri,Sat 10:00–15:00, 2026-09-01 → 2027-12-31 | 475137597224552142 | library site down (504); hours from konsthall page, Mon-Sat 10-15 window |
| 23 | Sörmlands museum | Nyköping | Sörmlands museum | Tue,Wed,Thu,Fri,Sat,Sun 10:00–17:00, 2026-09-01 → 2027-12-31 | 475128363472684647 | org Sörmlands museum (gov, Region Sörmland); Tue-Sun 10-17 |
| 24 | Nynäs slott & naturreservat | Nyköping | Region Sörmland | Daily always open, 2026-09-01 → 2027-12-31 | 475128436403242618 | org Region Sörmland; always open (reserve + grounds), castle summer only |
| 25 | Naturum Stendörren | Nyköping | Länsstyrelsen Södermanland | Wed,Thu,Fri,Sat,Sun 11:00–16:00, 2027-05-01 → 2027-10-04 | 475128722026956433 | 2027 copied from 2026 span 1 May-4 Oct; image only 770x420 official |
| 34 | Å-promenaden och Nyköpings hamn | Nyköping | Nyköpings kommun | Daily always open, 2026-09-01 → 2027-12-31 | 475128804117874335 | renamed Å-promenaden och Nyköpings hamn; org Nyköpings kommun |
| 27 | Femörefortet | Oxelösund | Föreningen Femörefortet | Sat,Sun 11:00–15:30, 2027-05-16 → 2027-10-04 | 475129595792754350 | 2027 copied 16 May-4 Oct weekends; older official visitor photo |
| 28 | Ramdalens Sportcenter | Oxelösund | Medley | Daily 09:00–16:00, 2026-09-01 → 2027-12-31 | 475129678940636867 | org Medley reused |
| 15 | Östra Södermanlands Järnväg – Mariefred station | Strängnäs | Museiföreningen Östra Södermanlands Järnväg | Sat,Sun 11:00–16:50, 2027-05-01 → 2027-08-29 | 475141574003557815 | 2027 copied 1 May-29 Aug weekends 11-16:50; FB url percent-encoded |
| 16 | Arsenalen – Sveriges Försvarsfordonsmuseum | Strängnäs | Stiftelsen Södermanlands militärhistoriska samlingar | Wed,Thu,Fri,Sat,Sun 11:00–16:00, 2026-09-01 → 2027-12-31 | 475141297389208915 | Wed-Sun 11-16 year-round; white logo on dark |
| 17 | Mälsåkers slott | Strängnäs | Föreningen Mälsåkers Framtid | Fri,Sat,Sun 11:00–16:00, 2027-06-12 → 2027-08-29 | 475140596328072457 | 2027 copied 12 Jun-29 Aug Fri-Sun 11-16 |
| 18 | Åkers bruksmuseum | Strängnäs | Åkers hembygdsförening | Sat,Sun 12:00–15:00, 2027-06-19 → 2027-08-29 | 475140660895188181 | 2027 copied 19 Jun-29 Aug weekends 12-15; address inferred (Bruksallén 17) |
| 19 | Larslunda simhall | Strängnäs | Strängnäs kommun | Daily 10:00–17:30, 2026-09-01 → 2027-12-31 | 475140747289462105 | org Strängnäs kommun created; daily 10-17:30 |
| 21 | Callanderska gården | Strängnäs | Mariefreds hembygdsförening | Sat,Sun 11:30–16:30, 2027-05-22 → 2027-08-29 | 475140926663067115 | 2027 based on last verified 2025 hours (weekends 11:30-16:30) |
| 22 | Ulvhälls hällar | Strängnäs | Ulvhälls hällar | Daily always open, 2026-09-01 → 2027-12-31 | 475140994367521979 | always open art park; no phone/email (only named curator) |
| 30 | Trosa gamla stad | Trosa | Trosa kommun | Daily always open, 2026-09-01 → 2027-12-31 | 475122076622030461 | org Trosa kommun created; always open |
| 31 | Trosa Aktivitetspark | Trosa | Trosa Aktivitetspark AB | Sat,Sun 10:00–17:00, 2026-09-01 → 2026-11-05 | 475122303231887078 | weekends 10-17 until 2026-11-05 (renew 2027) |
| 32 | Skärgårdstrafik Trosa – Trosa Gästhamn | Trosa | Apelago Group AB | Daily 10:00–16:00, 2027-06-11 → 2027-08-09 | 475122663673595736 | 2027 copied from 2026 span 11 Jun-9 Aug; img crop a=left (phone no. on hull removed) |
| 40 | Säfstaholms slott | Vingåker | Vingåkers kommun | Tue,Wed,Thu,Fri 11:00–16:00, 2026-09-01 → 2027-12-31 | 475138004885735177 | org Vingåkers kommun created; Tue-Fri 11-16 year-round |
| 42 | Hjälmargården & Läppe Camping | Vingåker | Hjälmargården | Daily always open, 2027-04-15 → 2027-09-19 | 475138061374621616 | 2027 season officially announced 15 Apr-19 Sep; legal entity to verify |
| 43 | Båsenbergabacken | Vingåker | Båsenberga Slalomklubb | Sat,Sun 10:00–16:00, 2027-02-06 → 2027-03-14 | 475138128844194916 | 2027 copied 6 Feb-14 Mar weekends 10-16 (snow dependent) |

## Skipped (9)

| # | Place | Kommun | Reason |
|---|---|---|---|
| 10 | Hop N Pop Trampolinpark | Eskilstuna | permanently closed (bankruptcy April 2025) |
| 20 | Grassagården | Strängnäs | no published museum hours; year-round part is a private café |
| 26 | Stadsparken Nyköping | Nyköping | no park with that name exists; area covered by Å-promenaden (34) |
| 29 | St Botvids kyrka | Oxelösund | not family relevant (church, no standing family offer) |
| 33 | Trosa Stadshotell & Spa | Trosa | not family relevant (adult hotel/spa, spa 18+) |
| 41 | Vingåkersbadet | Vingåker | closed for renovation until ~March 2027, new hours not published |
| 48 | Museet Malmahed | Flen | no confirmed 2026/2027 opening period, thin sources, only image has large text |
| 50 | Elektron (Gnesta) | Gnesta | not a drop-in place: municipal building with cinema, open only at screenings |
| 100 | Degerfors Hembygdsgård Knutsbol | Degerfors | association held its "last annual meeting" Feb 2026, old domain now spam; status unverified |

## Follow-ups
- **Seasons copied from 2026 into 2027 (update when official dates come out):** Skärgårdstrafik Trosa, Julita gård,
  Skottvångs Grufva, Naturum Stendörren, Femörefortet, Museispårvägen, Sparreholms bilmuseum, ÖSlJ, Mälsåkers slott,
  Åkers bruksmuseum, Callanderska gården (2025 pattern), Båsenbergabacken (snow dependent).
- **Ends soon:** Trosa Aktivitetspark (2026-11-05) — add the 2027 season when published; Backavallen skating (2027-04-04).
- **Re-check later:** Vingåkersbadet (reopens ~March 2027), Museet Malmahed (needs 2027 dates), Knutsbol (association status),
  Grassagården (summer guided tours), Elektron/Biograf Aniara and St Botvids kyrka family activities → as dated events instead.
- **Verify:** Backavallen public skating fee (not stated → isFree false), Kulturhuset Ängeln library hours (site was 504),
  Hjälmargården legal entity, Åkers bruksmuseum street address (inferred).
- **Existing data issues found (not changed):** Leo's Lekland Borås event (435898123416537027) is attached to a Huddinge place;
  Bohus fästning sits under Göteborg kommun; Statens fastighetsverk org has isGovernment false + Hagaparken website;
  the Jönköping batch uses parentMaxAge 18.

## Sheet
"Events" tab (gid 1719318267) refreshed: **1465 live events** (1280 recurring, 185 one time), rows A2:E1466;
region Total (G23) = 1465, city Total (I292) = 1465; Södermanland = 44, 237 cities have events.
