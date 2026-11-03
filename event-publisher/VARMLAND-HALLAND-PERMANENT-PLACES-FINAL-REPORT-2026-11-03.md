# Värmland + Halland — Permanent Places → Events — FINAL REPORT
**Date:** 2026-11-03
**Source:** `Famies - Vad ska vi hitta pa idag_1.html` (1201 places). Värmland 70 + Halland 51 = 121 places.
**Flow per place:** duplicate check → Organizer → Venue → Event (POST /admin/organizations → /admin/places → /admin/events), `shouldNotifyUsers: false` on every event.

## Result

| | Count |
|---|---|
| Places in the HTML (Värmland 70, Halland 51) | 121 |
| Already in the app (Mariebergsskogen, Värmlands Museum, Picassoskulpturen, Arvika Fordonsmuseum, Torsby Finnskogscentrum, Tjolöholms slott, Varbergs fästning, Tylösand) | 8 |
| Researched (14 parallel research agents) | 113 |
| **Published (organizer + venue + event)** | **88** |
| Skipped (reasons below) | 25 |
| Värmland live events after the run | 59 (5 + 54) |
| Halland live events after the run | 37 (3 + 34) |

## Final audit (API re-fetch of all published events): 0 issues
- place published, municipality set and correct, event linked to its venue
- parent 18–100, childMaxAge 18 (childMinAge 3 JumpYard/Kungsbygget, 7 Gokarthallen — real limits)
- `isRecurring` + recurrence on all; window open on every listed day; no event ends in the past
- 2 interests on all; ctaText "Läs mer" + official ctaLink; descriptions 300–650 chars, Swedish, official facts only
- 0 duplicate titles in the whole app; 0 duplicate / near-duplicate images (dHash among the new ones and against all chain events in the app) + visual contact sheet
- images re-uploaded to fammap S3, venue and event uploaded separately; organizer logos checked visually (white logos on a dark background)
- privacy: no personal-name emails or private mobiles (several left out on purpose; mobiles only where they are the business's own listed line)

## Published

| # | Region | Venue | Kommun | Organizer | Recurrence | Event ID | Notes |
|---|---|---|---|---|---|---|---|
| 28 | Halland | Klitterbadet | Falkenberg | Falkenbergs kommun (created) | Mon,Tue,Wed,Thu,Sat 14:00–17:30, 2026-09-01 → 2027-12-31 | 486681353371288600 |  |
| 29 | Halland | Rian designmuseum | Falkenberg | Falkenbergs kommun (reused) | Sun,Wed,Thu,Fri,Sat 12:00–16:00, 2026-09-01 → 2026-12-27 | 486681415514096672 |  |
| 30 | Halland | Toveks Bilmuseum | Falkenberg | Toveks Bil Falkenberg (created) | Mon,Tue,Wed,Thu,Fri 09:00–18:00, 2026-09-01 → 2027-12-31 | 486681482832675881 |  |
| 31 | Halland | Svedinos Bil- och Flygmuseum | Falkenberg | Svedinos Bil- och Flygmuseum AB (created) | Sun,Sat 11:00–16:00, 2027-03-26 → 2027-10-31 | 486681557575173170 | season copied from 2026 |
| 35 | Halland | Falkenbergs Bowlinghall | Falkenberg | Falkenbergs Bowlinghall (created) | Daily 15:00–18:00, 2026-09-01 → 2027-12-31 | 486681632636437570 |  |
| 36 | Halland | Gunnagård | Falkenberg | Gunnagård (created) | Sun,Sat 11:00–16:00, 2027-07-08 → 2027-11-01 | 486681728207848523 | season copied from 2026 |
| 40 | Halland | Halmstad slott | Halmstad | Statens fastighetsverk (reused (already in app)) | Daily always open, 2026-09-01 → 2027-12-31 | 486679840125126593 |  |
| 41 | Halland | Hallands Konstmuseum | Halmstad | Hallands Konstmuseum (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–17:00, 2026-09-01 → 2027-12-31 | 486679911419905057 |  |
| 42 | Halland | Mjellby konstmuseum | Halmstad | Halmstads kommun (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 486679981196346486 |  |
| 43 | Halland | Friluftsmuseet Hallandsgården | Halmstad | Hallands Konstmuseum (reused) | Daily always open, 2026-09-01 → 2027-12-31 | 486680043221714120 |  |
| 44 | Halland | Halmstad Arena Bad | Halmstad | Halmstads kommun (reused) | Daily 12:00–17:30, 2026-09-01 → 2027-12-31 | 486680094543217947 |  |
| 45 | Halland | Leo's Lekland Halmstad | Halmstad | Leos Lekland Halmstad (created) | Daily 10:00–19:00, 2026-09-01 → 2027-12-31 | 486680171584193916 |  |
| 46 | Halland | Halmstad Aktivitetscenter | Halmstad | Halmstad Aktivitetscenter (created) | Daily 14:00–18:00, 2026-09-01 → 2027-12-31 | 486680633880380698 |  |
| 47 | Halland | Yoump Trampolinpark Halmstad | Halmstad | Yoump Halmstad (created) | Daily 12:00–18:00, 2026-09-01 → 2027-12-31 | 486680704587957604 |  |
| 48 | Halland | Gokarthallen i Halmstad | Halmstad | Gokarthallen i Halmstad (created) | Daily 14:00–18:00, 2026-09-01 → 2027-12-31 | 486680780873958856 |  |
| 49 | Halland | O'Learys Halmstad | Halmstad | O'Learys Halmstad (created) | Daily 16:00–21:00, 2026-09-01 → 2027-12-31 | 486680865791837714 |  |
| 51 | Halland | Wapnö Gård | Halmstad | Wapnö AB (created) | Daily 09:00–16:00, 2026-09-01 → 2027-12-31 | 486680934771361391 |  |
| 38 | Halland | Örnahallens Hälsocenter | Hylte | Hylte kommun (created) | Tue,Wed,Fri 14:00–18:00, 2026-09-01 → 2027-12-31 | 486679777286064057 |  |
| 9 | Halland | Äskhults by | Kungsbacka | Kungsbacka kommun (created) | Sun,Sat 11:00–16:00, 2027-05-02 → 2027-09-27 | 486680264815183329 | season copied from 2026 |
| 10 | Halland | Naturum Fjärås Bräcka | Kungsbacka | Kungsbacka kommun (reused) | Sun,Fri,Sat 11:00–15:00, 2026-09-01 → 2027-12-31 | 486680341730330235 |  |
| 12 | Halland | Kungsbacka Badhus | Kungsbacka | Medley (reused (already in app)) | Daily 09:00–17:00, 2026-09-01 → 2027-12-31 | 486680398118553369 |  |
| 13 | Halland | Fjärås Simhall | Kungsbacka | Medley (reused (already in app)) | Sun,Tue,Wed,Thu,Fri,Sat 12:00–15:30, 2026-09-01 → 2027-12-31 | 486680473850906561 |  |
| 14 | Halland | JumpYard Kungsbacka | Kungsbacka | JumpYard Kungsbacka (created) | Daily 10:00–19:00, 2026-09-01 → 2027-12-31 | 486680547855205479 |  |
| 52 | Halland | Teckningsmuseet | Laholm | Laholms kommun (created) | Daily 12:00–16:00, 2026-09-01 → 2027-12-31 | 486681018095404694 |  |
| 56 | Halland | Kungsbygget Adventure Park | Laholm | Kungsbygget Adventure Park (created) | Sun,Fri,Sat 11:00–16:00, 2027-04-02 → 2027-11-01 | 486681097829123892 | season copied from 2026 |
| 17 | Halland | Hallands kulturhistoriska museum | Varberg | Hallands kulturhistoriska museum (created) | Sun,Tue,Wed,Thu,Fri,Sat 12:00–16:00, 2026-09-01 → 2027-12-31 | 486683801863357590 |  |
| 19 | Halland | Världsarvet Grimeton Radiostation | Varberg | Världsarvet Grimeton (created) | Wed,Thu,Fri,Sat 10:00–15:00, 2026-09-01 → 2026-11-28 | 486683877444715687 |  |
| 20 | Halland | Naturum Getterön | Varberg | Länsstyrelsen Halland (created) | Sun,Tue,Wed,Thu,Fri,Sat 10:00–16:00, 2026-09-01 → 2027-12-31 | 486683958487057608 |  |
| 21 | Halland | Åkulla bokskogar | Varberg | Länsstyrelsen Halland (reused) | Daily always open, 2026-09-01 → 2027-12-31 | 486684021049296098 |  |
| 22 | Halland | Pingvinen Varberg | Varberg | Medley (reused (already in app)) | Daily 09:00–17:00, 2026-09-01 → 2027-12-31 | 486684067757065476 |  |
| 24 | Halland | Läjet – Träslövsläge fiskehamn och badstrand | Varberg | Varbergs kommun (created) | Daily always open, 2026-09-01 → 2027-12-31 | 486684136820475167 |  |
| 25 | Halland | Varbergs Tropikarium | Varberg | Varbergs Tropikarium (created) | Sun,Sat 10:00–15:00, 2027-04-03 → 2027-11-01 | 486684208979281195 | season copied from 2026 |
| 26 | Halland | Öströö Fårfarm | Varberg | Öströö Fårfarm (created) | Sun,Fri,Sat 11:00–15:00, 2026-09-01 → 2027-12-31 | 486684282715145526 |  |
| 27 | Halland | Kulturhuset Komedianten | Varberg | Varbergs kommun (reused) | Daily 12:00–16:00, 2026-09-01 → 2027-12-31 | 486684360259437902 |  |
| 89 | Värmland | Rackstadmuseet | Arvika | Ideella Föreningen Rackstadmuseet (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 486681803722097773 |  |
| 90 | Värmland | Klässbols Linneväveri – väveri och fabriksbutik | Arvika | Klässbols Linneväveri AB (created) | Mon,Tue,Wed,Thu,Fri,Sat 10:00–16:00, 2026-09-01 → 2027-12-31 | 486681866267559025 |  |
| 91 | Värmland | Såguddens friluftsmuseum | Arvika | Västra Värmlands Fornminnesförening (created) | Daily always open, 2026-09-01 → 2027-12-31 | 486681950170416254 |  |
| 92 | Värmland | Arvika simhall | Arvika | Arvika kommun (created) | Daily 12:00–15:00, 2026-09-01 → 2027-12-31 | 486682025172960386 |  |
| 93 | Värmland | Arvika Konsthall | Arvika | Arvika Konstförening (created) | Tue,Wed,Thu,Fri 12:00–16:00, 2026-09-01 → 2027-12-31 | 486682090587325574 |  |
| 94 | Värmland | Minigolfparken i Arvika | Arvika | Minigolfparken i Arvika (created) | Daily 12:00–18:00, 2027-04-01 → 2027-09-30 | 486682191200289930 | season copied from 2026 |
| 95 | Värmland | Arvika Kanot och Turistcenter | Arvika | Arvika Kanot och Turistcenter (created) | Daily 10:00–16:30, 2027-05-15 → 2027-09-15 | 486682275145090190 |  |
| 96 | Värmland | Glaskogens Infocenter och Kanotcentral, Lenungshammar | Arvika | Stiftelsen Glaskogens naturreservat (created) | Daily 10:00–17:00, 2027-03-30 → 2027-09-30 | 486682348436358290 | season copied from 2026 |
| 97 | Värmland | Eda skans | Eda | Statens fastighetsverk (reused (already in app)) | Daily always open, 2026-09-01 → 2027-12-31 | 486674988229756194 |  |
| 98 | Värmland | Fredsmonumentet i Morokulien | Eda | Eda kommun (created) | Daily always open, 2026-09-01 → 2027-12-31 | 486675060640220454 |  |
| 99 | Värmland | Eda Glasmuseum | Eda | Eda Glasbruksförening (created) | Daily 10:00–17:00, 2027-05-01 → 2027-09-30 | 486675165590095146 | season copied from 2026 |
| 100 | Värmland | Valfjället Skicenter | Eda | Valfjället Skicenter AB (created) | Sun,Fri,Sat 10:00–16:00, 2026-12-19 → 2027-04-04 | 486675254660334894 |  |
| 81 | Värmland | Långbans Gruvby | Filipstad | Värmlands Museum (reused (already in app)) | Daily 10:00–16:00, 2027-06-06 → 2027-08-23 | 486675713424917925 | season copied from 2026 |
| 82 | Värmland | Lesjöfors Museum | Filipstad | Värmlands Museum (reused (already in app)) | Daily 10:00–16:00, 2027-06-06 → 2027-08-23 | 486675782958089650 | season copied from 2026 |
| 83 | Värmland | Spångbergshallen Bad | Filipstad | Filipstads kommun (created) | Tue,Wed,Fri,Sat 14:00–16:00, 2026-09-01 → 2027-12-31 | 486675872842024384 |  |
| 72 | Värmland | Klarälvsbadet | Forshaga | Forshaga kommun (created) | Tue,Wed,Thu,Fri 15:00–19:00, 2026-09-01 → 2027-12-31 | 486679704951097263 |  |
| 85 | Värmland | Grums bad- och sporthall | Grums | Grums kommun (created) | Tue,Wed,Fri 16:00–18:45, 2026-09-01 → 2027-12-31 | 486675948716983819 |  |
| 118 | Värmland | Hagfors Järnvägsmuseum | Hagfors | Hagfors Järnvägsmuseum (created) | Sun,Tue,Wed,Thu,Fri,Sat 10:00–17:00, 2027-06-13 → 2027-08-31 | 486668640536528531 | season copied from 2026 |
| 119 | Värmland | Värmlands Älgpark | Hagfors | Värmlands Älgpark (created) | Sun,Wed 11:00–13:00, 2026-11-11 → 2027-03-01 | 486669065931228823 |  |
| 71 | Värmland | Skoghalls bangolf | Hammarö | Skoghalls Bangolfklubb (created) | Daily 09:00–21:00, 2027-04-18 → 2027-08-31 | 486679639880664993 | season copied from 2026 |
| 57 | Värmland | Sandgrund Lars Lerin | Karlstad | Sandgrund Lars Lerin (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 486678068828604101 |  |
| 58 | Värmland | Brigadmuseum | Karlstad | Brigadmuseum (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 486678149057251031 |  |
| 59 | Värmland | Alsters herrgård | Karlstad | Karlstads kommun (created) | Daily always open, 2026-09-01 → 2027-12-31 | 486678222214301417 |  |
| 61 | Värmland | Sundstabadet | Karlstad | Karlstads kommun (reused) | Daily 10:00–18:00, 2026-09-01 → 2027-12-31 | 486678276572481278 |  |
| 62 | Värmland | Tingvalla isstadion | Karlstad | Karlstads kommun (reused) | Mon,Tue,Thu,Fri 09:00–15:00, 2026-09-01 → 2026-12-22 | 486678330528007951 |  |
| 63 | Värmland | Leo's Lekland Karlstad | Karlstad | Leos Lekland Karlstad (created) | Daily 10:00–19:00, 2026-09-01 → 2027-12-31 | 486678415051622177 |  |
| 64 | Värmland | JumpYard Karlstad | Karlstad | JumpYard Karlstad (created) | Daily 10:00–18:00, 2026-09-01 → 2027-12-31 | 486678490045777715 |  |
| 66 | Värmland | Bowling på Nöjesfabriken | Karlstad | Nöjesfabriken (created) | Tue,Wed,Thu,Fri,Sat 14:00–19:00, 2026-09-01 → 2027-12-31 | 486679278767867719 |  |
| 67 | Värmland | O'Learys Karlstad | Karlstad | O'Learys Karlstad (created) | Sun,Mon,Tue,Fri,Sat 16:00–22:00, 2026-09-01 → 2027-12-31 | 486679343469201241 |  |
| 68 | Värmland | Karlstads 4H-gård | Karlstad | Karlstad 4H (created) | Daily 09:00–15:30, 2026-09-01 → 2027-12-31 | 486679425266517867 |  |
| 69 | Värmland | Båtbussarna – Inre hamn Karlstad | Karlstad | Värmlandstrafik (created) | Daily 10:00–19:45, 2027-06-08 → 2027-08-30 | 486679497358215037 | season copied from 2026 |
| 70 | Värmland | Karlstad Sightseeing – sightseeingtåget på Stora torget | Karlstad | Karlstad Sightseeing AB (created) | Daily 10:00–16:30, 2027-06-01 → 2027-08-31 | 486679565524043663 | season copied from 2026 |
| 74 | Värmland | Kristinehamn Arena – badhuset | Kristinehamn | Kristinehamn Arena (created) | Daily 09:00–16:00, 2026-09-01 → 2027-12-31 | 486672510377559711 |  |
| 75 | Värmland | Lek & Luft – Kristinehamn Arena | Kristinehamn | Kristinehamn Arena (reused) | Sun,Mon,Tue,Wed,Fri,Sat 10:00–15:00, 2026-12-28 → 2027-01-06 | 486672566270854920 |  |
| 76 | Värmland | Kristinehamns konstmuseum | Kristinehamn | Kristinehamns kommun (created) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–16:00, 2026-09-01 → 2027-12-31 | 486672632146593650 |  |
| 77 | Värmland | Kristinehamns Historiska museum | Kristinehamn | Kristinehamns kommun (reused) | Tue,Wed,Thu,Fri 10:00–16:00, 2026-09-01 → 2027-12-31 | 486672693886748634 |  |
| 78 | Värmland | Bowlingen i Kristinehamn | Kristinehamn | Bowlingen i Kristinehamn (created) | Sun,Tue,Wed,Thu,Fri,Sat 14:00–18:00, 2026-09-01 → 2027-12-31 | 486672758588081221 |  |
| 79 | Värmland | Stadsbondgården vid Östervik | Kristinehamn | Kristinehamns kommun (reused) | Daily always open, 2026-09-01 → 2027-12-31 | 486672819866862767 |  |
| 120 | Värmland | Gamla Brukets museer | Munkfors | Föreningen Gamla Bruket i Munkfors (created) | Daily 11:00–17:00, 2027-07-01 → 2027-08-31 | 486669146537363099 | season copied from 2026 |
| 104 | Värmland | Rottneros Park | Sunne | Rottneros Park Trädgård AB (created) | Daily 10:00–16:00, 2027-05-30 → 2027-09-06 | 486673769381790990 | season copied from 2026 |
| 105 | Värmland | Selma Lagerlöfs Mårbacka | Sunne | Mårbackastiftelsen (created) | Daily 12:00–16:00, 2027-06-13 → 2027-08-23 | 486673852227683602 | season copied from 2026 |
| 106 | Värmland | Sunne Sommarland | Sunne | Sunne Sommarland (created) | Daily 10:00–17:00, 2027-06-20 → 2027-08-09 | 486673922406778135 | season copied from 2026 |
| 107 | Värmland | Sunne Ski & Bike | Sunne | Sunne Ski & Bike (created) | Sun,Fri,Sat 09:30–15:30, 2026-12-26 → 2027-03-28 | 486673995127620891 |  |
| 109 | Värmland | Tossebergsklätten | Sunne | Sunne kommun (created) | Daily always open, 2026-09-01 → 2027-12-31 | 486674074836174111 |  |
| 87 | Värmland | Säffle simhall | Säffle | Säffle kommun (created) | Sun,Mon,Tue,Wed,Fri,Sat 12:00–15:00, 2026-09-01 → 2027-12-31 | 486676040429635129 |  |
| 88 | Värmland | von Echstedtska gården | Säffle | Värmlands Museum (reused (already in app)) | Sun,Tue,Wed,Thu,Fri,Sat 11:00–18:00, 2027-06-23 → 2027-08-16 | 486676114794645103 | season copied from 2026 |
| 111 | Värmland | Branäs | Torsby | Branäs Fritidscenter AB (created) | Daily 09:00–19:00, 2026-12-11 → 2027-04-04 | 486676502809708198 |  |
| 112 | Värmland | Torsby Skidtunnel & Sportcenter | Torsby | Torsby kommun (created) | Daily 09:00–17:00, 2026-09-01 → 2027-01-31 | 486676572636481210 |  |
| 114 | Värmland | Hovfjället | Torsby | Hovfjället AB (created) | Daily 09:30–15:00, 2026-12-19 → 2027-03-28 | 486676671051630269 |  |
| 115 | Värmland | TorsbyBadet | Torsby | Torsby kommun (reused) | Mon,Tue,Wed,Thu,Fri 14:00–18:00, 2026-09-01 → 2027-05-02 | 486676732800173759 |  |
| 116 | Värmland | Torsby Fordonsmuseum | Torsby | Torsby Fordonsmuseum (created) | Daily 12:00–17:00, 2027-06-01 → 2027-08-31 | 486676821862024898 | season copied from 2026 |
| 101 | Värmland | Årjängs Bad- och friskvårdscenter | Årjäng | Årjängs kommun (created) | Mon,Tue,Wed,Thu,Fri 15:00–17:30, 2026-09-01 → 2027-12-31 | 486675341381764402 |  |
| 102 | Värmland | Nordiska Travmuseet | Årjäng | Nordiska Travmuseet (created) | Mon,Tue,Wed,Thu,Fri 12:00–16:00, 2026-09-01 → 2027-12-31 | 486675431794181462 |  |
| 103 | Värmland | Årjängstrollet | Årjäng | Årjängs kommun (reused) | Daily always open, 2026-09-01 → 2027-12-31 | 486675484986344833 |  |

## Skipped

| # | Region | Place | Kommun | Reason |
|---|---|---|---|---|
| 32 | Halland | Morups fyr & Fyr- och fiskemuseum | Falkenberg | no fixed opening hours – lighthouse and Fyr- & Fiskerimuseum open only on ~14 scheduled public showing days a year (otherwise bookable private showings only) |
| 33 | Halland | Gekås Ullareds Adventure Park | Falkenberg | no published opening hours or season – activities run in pre-booked time slots and the booking calendar (biljett.app.gekas.se) is not publicly readable; re-check in sprin |
| 34 | Halland | Falkenbergs Motorbana Gokart | Falkenberg | no fixed opening hours – drop-in only at certain ad-hoc times during the summer holiday (announced on the club's site/socials, can be cancelled for rain); otherwise pre-b |
| 37 | Halland | Franks Äventyrspark | Falkenberg | no published opening hours or season dates – outdoor park closed for 2026, 2027 opening not announced, and neither the park site nor Visit Falkenberg states hours (both s |
| 50 | Halland | Halmstads Teater | Halmstad | Performance venue only: no drop-in visit or fixed opening hours; doors open one hour before each performance (ticketed events, publish as single events instead) |
| 39 | Halland | Hultagärdsbacken | Hylte | no current official source: own site hultagardsbacken.se no longer resolves (last archived 2018), only a 2023 Visit Hylte news item mentions it; snow-dependent with no fi |
| 11 | Halland | Onsala rymdobservatorium | Kungsbacka | No drop-in visits: official Chalmers page says 'Vi tar endast emot bokade besök' - visitor centre open only at booked times (group/school study visits on weekdays) plus a |
| 15 | Halland | Nordhallands Hembygdsmuseum | Kungsbacka | No verifiable official photo of the museum: hembygd.se (the only source with museum photos) returns HTTP 403 to non-browser requests incl. its image host, and visitkungsb |
| 16 | Halland | Kungsbacka ishall | Kungsbacka | No real photo of the ice hall on any official source: kungsbacka.se and visitkungsbacka.se only use generic outdoor natural-ice skating photos (girl on lake ice, skates o |
| 53 | Halland | Laholms Keramikmuseum | Laholm | Merged: housed on the lower floor of Teckningsmuseet (same building, entrance, hours and organizer Laholms kommun); covered by the Teckningsmuseet event (i52) to avoid a  |
| 54 | Halland | Laholms Teater | Laholm | Performance/rental venue only: no drop-in visit or opening hours; open only for scheduled concerts and shows listed in the visitlaholm.se event calendar (publish those as |
| 55 | Halland | Folkhälsocentrum Laholm (simhall) | Laholm | No real photo of the swim hall found on any official source (laholm.se simhall page has no photos; nothing on visitlaholm.se, Naturkartan or Laholmshem). All other data b |
| 18 | Halland | Kallbadhuset Varberg | Varberg | Not a family place: cold-bath/sauna house with nakenbad in separate women's/men's sections (spa type). Also changing operator at New Year; closed 1 Jan–31 Mar 2027 for re |
| 23 | Halland | Varbergs Bowlinghall | Varberg | No real photo of the place on any official source: varbergsbowlinghall.se only has a generic black-and-white ball close-up banner (1400x400) and an illustration, Visit Va |
| 84 | Värmland | John Ericssons mausoleum | Filipstad | not a family visitor place: grave chapel on Östra kyrkogården (cemetery) with no family offer, no visitor operation or opening hours, interior not open; only one official |
| 86 | Värmland | Sliperiet i Borgvik | Grums | not family relevant + no verifiable hours: contemporary art/photo konsthall (Anton Corbijn 2026) with restaurant, no family/kids offer; exhibition season ended 6 Sep 2026 |
| 60 | Värmland | Wermland Opera – Karlstads teater | Karlstad | Not a drop-in place: the theatre building only opens for performances (box office in Operahuset open helgfria onsdagar 14–17 only; no public guided tours/drop-in visits f |
| 65 | Värmland | Escape Room Karlstad – BrainGear | Karlstad | booking only (Bookeo), no published opening hours anywhere official (braingear.se, Visit Värmland says 'see their website'); no drop-in visit. Data below is complete if h |
| 73 | Värmland | Gokart i Kil | Kil | no fixed hours: booking only, with drop-in for just one summer week (v.30 in 2026). Season is over and 2027 is not announced. No real photo of the track exists officially |
| 121 | Värmland | Geijersgården | Munkfors | No regular opening hours / no real drop-in: open to drop-in visitors only during the 4-day Kulturvecka (30 Jul–2 Aug 2026, guided tours 11:00 and 14:00); otherwise only p |
| 80 | Värmland | Värmlands brandhistoriska museum – Spruthuset | Storfors | no confirmed public opening hours: the operator (Värmlands Brandhistoriska Klubb) only offers group visits on request (min. 10 people, not in winter); its 2023–24 annual  |
| 108 | Värmland | Sundsbergs gård | Sunne | not family relevant: café, art gallery (konsthall) and small museums (farm, textile, dentist, forest) with no children's offer on the official site; a kids' line (rabbits |
| 110 | Värmland | Vallarnas alpackor | Sunne | no drop-in visit: every activity (guided alpaca viewing, alpaca walk, fika in the paddock) must be booked in advance, and the FAQ says it is not possible to come by witho |
| 113 | Värmland | Vildmark i Värmland – timmerflotte på Klarälven | Torsby | Not a drop-in place: timber raft trips are prebooked packages only ('måste förbokas'), start 09:00 on set start days 5 Jun–21 Aug 2027 from Klarälvens Camping, no opening |
| 117 | Värmland | Sahlströmsgården | Torsby | Not a family drop-in place: today mainly hotel, restaurant and conference venue; the artist home (mangårdsbyggnaden) is 'endast öppen för guidad visning och enligt överen |

## Follow-ups
- **Seasons copied from 2026 into 2027 (20 places, marked above):** update when the official 2027 dates are out.
- **Ends soon — add the next period when it is published:** Grimeton (2026-11-28), Tingvalla isstadion skating (2026-12-22),
  Rian designmuseum (2026-12-27), Torsby Skidtunnel (2027-01-31), Lek & Luft Kristinehamn (jullov only, 2027-01-06),
  TorsbyBadet (high-season hours to 2027-05-02).
- **Check:** Värmlands Älgpark (bookings reopen "end of November", event starts 11 Nov per the timetable), Eda Glasmuseum
  (2027 hours from an undated Visit Värmland page), O'Learys Karlstad (Wed/Thu hours disagree between sources),
  Falkenbergs Bowlinghall (hours read from one booking week).
- **Could be published later:** Nordhallands Hembygdsmuseum, Kungsbacka ishall, Folkhälsocentrum Laholm, Varbergs Bowlinghall
  (all data is ready, only real photos are missing); Morups fyr and Onsala rymdobservatorium public days as dated events.
- **Organizer avatars left empty on purpose:** Hallands Konstmuseum (the logo file on its site shows Hallands Kulturhistoriska
  Museum), Eda Glasbruksförening, Västra Värmlands Fornminnesförening, Arvika Konstförening, Minigolfparken i Arvika,
  Klässbols Linneväveri (no usable logo), Bowlingen i Kristinehamn (logo blocked).
- **Existing data issue found (not changed):** one existing chain event (Leo's/JumpYard/O'Learys/Yoump group) uses an
  images.unsplash.com image instead of an S3 upload.

## Sheet
"Events" tab (gid 1719318267) refreshed: **1484 published live events**, rows A2:E1485, 30/30 chunk hashes match;
region Total (G23) = 1484, city Total (I292) = 1484; Värmland 59, Halland 37.
