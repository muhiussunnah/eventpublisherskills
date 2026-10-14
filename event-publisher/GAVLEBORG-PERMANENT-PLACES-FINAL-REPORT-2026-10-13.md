# Gävleborg — Permanent Places → Events — FINAL REPORT
**Date:** 2026-10-13
**Source:** `0912Famies - Vad ska vi hitta pa idag.html` (embedded `places`, region = Gävleborg, 62 places)
**Flow per place:** duplicate check → Organizer → Venue → Event (POST /admin/organizations → /admin/places → /admin/events)

## Result

| | Count |
|---|---|
| Gävleborg places in the HTML | 62 |
| Already in the app before this session (Furuvik, Vildriket, Hälsinglands museum, Högbo Bruk) | 4 |
| Internal duplicate in the HTML (#22 "Vildriket (Järvzoo)" = #1) | 1 |
| Unique candidates | 57 |
| **Published (organizer + venue + event)** | **52** |
| Skipped (reasons below) | 5 |
| Gävleborg events live after the run | 56 (4 + 52) |

New organizers created: 28, plus reused existing ones (Statens fastighetsverk, and kommun organizers created once in this run and shared).

## Final audit (API re-fetch of all 56 Gävleborg events): 0 issues
- 0 duplicate titles, 0 duplicate images (each event has its own S3 upload; in-session SHA-256 dedup)
- municipality set on every place (Gävle, Sandviken, Hofors, Ockelbo, Ljusdal, Ovanåker, Hudiksvall, Nordanstig, Söderhamn, Bollnäs)
- `shouldNotifyUsers: false` on every POST (push off)
- parentMinAge 18 / parentMaxAge 100; childMaxAge 18; no childMinAge 1
- `isRecurring` + recurrence on all; no event ends in the past
- ctaText "Läs mer" + official ctaLink on all; 2 interests on all
- descriptions 400–560 chars, plain Swedish prose, no code/markdown
- All images uploaded to fammap S3 (no hotlinks); visual check of all 52 images and 29 avatars done

## Published (52)

| # | Event (venue) | Kommun | Organizer | Recurrence | Event ID |
|---|---|---|---|---|---|
| 4 | Järnvägsmuseet | Gävle | Järnvägsmuseet (gov) | Tue–Sun 11–17, year-round | 471554038639396410 |
| 5 | Fjärran Höjderbadet | Gävle | Gävle kommun | Daily 10–17:30, year-round | 471554402545600087 |
| 6 | Länsmuseet Gävleborg | Gävle | Stiftelsen Länsmuseet Gävleborg | Tue–Sun 12–16 | 471554637854443124 |
| 7 | Sveriges Fängelsemuseum | Gävle | Föreningen Fängelsemuseet i Gävle | Wed–Sat 12–16 | 471554977509181073 |
| 8 | DOME Adrenaline Zone | Gävle | The Dome Adrenaline Zone | Daily 14–19 | 471555468267914926 |
| 9 | Gävle Klätterpark (ex Högt & Lågt) | Gävle | The Dome Adrenaline Zone | Summer 2027 daily 10–17 | 471555741375825610 |
| 10 | Gävle slott (exterior + slottspark) | Gävle | Statens fastighetsverk (existing) | Always open | 471569057376667573 |
| 11 | Boulognerskogen | Gävle | Gävle kommun | Always open | 471569401997461457 |
| 12 | O'Learys Gävle | Gävle | O'Learys Gävle | Daily 16–22 | 471569660341422062 |
| 13 | Joe Hill-gården | Gävle | Joe Hill-Sällskapet | Thu–Sat 12–16 | 471569880114562059 |
| 14 | Limön | Gävle | Gävle kommun | Always open (boat note in text) | 471570097647944743 |
| 15 | Parkbadet | Sandviken | Sandvikens kommun | Daily 10–17 | 471570400266978372 |
| 17 | Kungsberget | Sandviken | Kungsbergets Fritidsanläggningar AB | 21 Dec 2026–4 Apr 2027 daily 09–16 | 471570613228569686 |
| 18 | Hoforshallen Simhall (list said "Stålbadet") | Hofors | Hofors kommun | Tue/Wed/Fri/Sat 14–17, to 31 May 2027 | 471556819983042281 |
| 19 | Pelargonmuseum & Trädgård | Hofors | Pelargonmuseum & Trädgård i Torsåker | 27 Feb–31 Jul 2027 Wed–Sun 10–15 | 471557035201169170 |
| 20 | Wij Trädgårdar | Ockelbo | Stiftelsen Wij Trädgårdar | Summer 2027 daily 10–16 | 471557337895700279 |
| 21 | Jädraås–Tallås Järnväg | Ockelbo | Museisällskapet Jädraås-Tallås Järnväg | Summer 2027 Sundays from 10:15 | 471557623376807744 |
| 23 | Järvsö Bergscykelpark | Ljusdal | Järvsö Bergscykel Park AB | Fri–Sun 09:30–15, to 1 Nov 2026 | 471557928386594633 |
| 24 | Järvsöbacken | Ljusdal | Järvsöbacken AB | 18 Dec 2026–4 Apr 2027 daily 09–16 | 471558241684326223 |
| 25 | Stenegård | Ljusdal | Ljusdals kommun | Thu–Sat 11–16, year-round | 471558519078815572 |
| 26 | Världsarvsgården Bortom Åa | Ljusdal | Fågelsjö hembygdsförening | Summer 2027 daily 10–17 | 471559870642947931 |
| 27 | Världsarvsgården Bommars | Ljusdal | Hälsingegården Bommars i Letsbo | Summer 2027, booking only | 471560126763927390 |
| 28 | Färila sim- och sporthall | Ljusdal | Ljusdals kommun | Sat–Sun 10–16 | 471560499905988448 |
| 29 | Edsbyns museum | Ovanåker | Ovanåkers hembygdsförening | Mon–Fri 13–16 | 471560737681082211 |
| 30 | Världsarvsgården Pallars | Ovanåker | Världsarvsgården Pallars | Summer 2027 Mon/Wed/Fri 11:00 tour | 471561273469863783 |
| 31 | Världsarvsgården Jon-Lars | Ovanåker | Världsarvsgården Jon-Lars | Summer 2027 daily 12:00 tour | 471561329455433578 |
| 34 | Iggesunds Bruksmuseum | Hudiksvall | Stiftelsen Hudiksvalls Bruksminnen | Summer 2027 Mon–Fri 11–17 | 471562232690411373 |
| 35 | Hudik bad & relax | Hudiksvall | Hudiksvalls kommun | Mon/Wed/Thu/Fri 15–17, to 18 Jun 2027 | 471562616771217268 |
| 37 | Ystegårn i Hillsta | Hudiksvall | Ystegårn Café & Bistro | Daily 11–16 | 471562857440380794 |
| 38 | Malnbadens Camping | Hudiksvall | Malnbadens Camping | 13 May–30 Sep 2027 | 471563068489369472 |
| 39 | Hölick och Hornslandet | Hudiksvall | Länsstyrelsen Gävleborg | Always open | 471563389747890054 |
| 40 | Köpmanberget | Hudiksvall | Hudiksvalls kommun | Always open | 471563788970133387 |
| 41 | Avholmsberget | Hudiksvall | Hudiksvalls kommun | Always open | 471563837573728144 |
| 42 | Hassela Ski Resort | Nordanstig | Hassela Ski Resort AB | 23 Dec 2026–4 Apr 2027 daily 09–16 | 471546697592374776 |
| 43 | Trolska Skogen | Nordanstig | Trolska Skogen i Hälsingland ek. förening | 21 Nov–20 Dec 2026 Sat–Sun (Christmas show) | 471547984799106562 |
| 44 | Ersk-Matsgården | Nordanstig | Nordanstigs kommun | Summer 2027 Mon–Fri 12–16 | 471548430519404040 |
| 45 | Halls gård | Nordanstig | Halls Gårds Islandshästar | Year-round, booking only | 471549145656624651 |
| 46 | Mellanfjärden | Nordanstig | Nordanstigs kommun | Always open | 471549342973462032 |
| 47 | F15 Flygmuseum | Söderhamn | F15 Kamratförening | Tue–Sun 10–16 | 471549519838873110 |
| 48 | Oscarsborg | Söderhamn | Söderhamns kommun | Always open (viewpoint) | 471549786361726490 |
| 49 | Stenö Havsbad och Camping | Söderhamn | Söderhamns kommun | Summer 2027 daily | 471550091749000735 |
| 50 | Aquarena Hällåsen | Söderhamn | Söderhamns kommun | Tue/Wed/Fri/Sat/Sun 09:30–14:30, to 24 Jun 2027 | 471550382900807203 |
| 51 | Hälsingegården Erik-Anders | Söderhamn | Hälsingegården Erik-Anders | Summer 2027 daily 11–17 | 471550635666343464 |
| 52 | Teknikpark Mohed MTB | Söderhamn | Mo Aktivitetsförening | Always open | 471550920476362284 |
| 53 | Söderblomsgården | Söderhamn | Trönö hembygdsförening | Summer 2027 daily 11–17 | 471551153369286192 |
| 55 | Världsarvsgården Gästgivars | Bollnäs | Världsarvet Gästgivars AB | Summer 2027 daily 11–17 | 471565052839757718 |
| 56 | Träslottet | Bollnäs | Träslottet | Sat–Sun 11–15 | 471565270029207452 |
| 57 | Växbo Lin | Bollnäs | Växbo Lin AB | Mon–Sat 10–15 | 471565647231354785 |
| 58 | Växbo Kvarn | Bollnäs | Växbo Kvarn AB | Summer 2027 daily 11–17 | 471565717578221479 |
| 59 | Bollnäs simhall | Bollnäs | Bollnäs kommun | Daily 10–16, to 7 Jun 2027 | 471566019131901869 |
| 60 | Bollnäs museum och konsthall | Bollnäs | Bollnäs kommun | Tue/Wed/Fri 13–16, to 30 Oct 2026 | 471566377468069807 |
| 61 | Västerby – Hälsingegårdar i Rengsjö | Bollnäs | Rengsjö hembygdsförening | Always open (self-guided walk) | 471566434376386482 |

## Skipped (5)

| # | Place | Reason |
|---|---|---|
| 16 | Göransson Arena | No public opening hours; public-skating times not published; only text-heavy photos |
| 32 | Alfta sim- och sporthall | Closed to the public Sep–Dec 2026; spring 2027 undecided |
| 33 | Världens största skidor | No official source or owner; only image is an Atlas Obscura user photo |
| 36 | Hudiksvalls Teater | Rental venue only, no opening hours or own family programme |
| 54 | Ljusne inomhusbad | Not a public bath (babysim club courses + 18+ private rental) |

## Corrections vs. the HTML list
- "Stålbadet" does not exist → Hofors swim hall is **Hoforshallen Simhall**.
- "Högt & Lågt Gävle Klätterpark" → now **Gävle Klätterpark**, Hemlingbyvägen 93 (not Boulognerskogen).
- Sveriges Järnvägsmuseum calls itself **Järnvägsmuseet**.
- Joe Hill-gården (Nedre Bergsgatan 28) ≠ Joe Hill Visitor Center (inside Fängelsemuseet).
- Gävle slott is closed to the public; listed as exterior + slottspark.
- Coordinates were off for most places (up to 15 km) → replaced with OSM / official coordinates.
- Outdated domains: stenohavsbad.se → stenocamping.se; traslottet.se → traslottet.nu; hogtochlagt.se → gavleklatterpark.se.
- Edsbyns museum postcode 828 21 (not 828 33); Iggesunds Bruksmuseum on Ankarvägen, 825 30 (OSM).

## Recurrence rule used
One recurrence window that is genuinely open on **every** listed day (e.g. Aquarena weekends close 14:30, so 09:30–14:30). Full per-day hours are stored on the venue (`openingHours`). Always-open outdoor places: 00:00 + 1439 min. Seasonal places with ended 2026 season: 2027 window = same calendar span as 2026 when 2027 dates are not published yet.

## Needs a re-check later
- 2027 summer dates not announced yet (2026 span copied): Gävle Klätterpark, Wij, JTJ, Bortom Åa, Bommars, Pallars, Jon-Lars, Iggesund (start 28 Jun is an estimate), Ersk-Mats, Erik-Anders, Söderblomsgården, Stenö, Gästgivars, Växbo Kvarn, Malnbaden (end date).
- Ends soon, extend when new period is announced: Bollnäs museum (30 Oct 2026), Bergscykelpark (1 Nov 2026), Trolska Skogen (20 Dec 2026, summer 2027 not announced).
- Fjärran Höjderbadet: gavle.se was unreachable from here; contact/hours from Wayback (Jan–Jul 2026) + visitgavle.
- Entrance fee unverified (set isFree=false): Söderblomsgården, Edsbyns museum, Iggesund, Ystegårn.
- O'Learys Gävle image is the official photo on olearys.com/gaevle (chain photo, not used on any other event).

## Privacy choices
Personal-name emails and private individuals' mobiles were not published (Halls gård email, Ersk-Mats staff email, Pallars/Jon-Lars guide phones, Iggesund guide phone, Söderblomsgården gmail, Avholmsberget café mobile). Only generic/business contacts were used.

## Observations outside this task (not changed)
- Existing organizer **Statens fastighetsverk** has `isGovernment: false` and website pointing to the Hagaparken page.
- The 2026-10-01 Jönköping-region batch uses `parentMaxAge: 18`; dashboard default and memory rule P are 100 — worth an audit.
- One failed organizer create (Järnvägsmuseet, email unique-conflict with "Sjöhistoriska") may have left an unused SMTF logo file in S3.
