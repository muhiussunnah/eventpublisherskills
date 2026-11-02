# Monday report — 2 November 2026

Source: FamMap admin API (scan of all 1420 live events, 0 failures) + sheet `Weekly_Events_Update`.
Published live events match the dashboard's "Published Events" card (1,397).

| Number | This week | 20 Oct report | Change |
|---|---:|---:|---:|
| Events live (published) | 1,397 (1,306 ongoing + 91 upcoming) | 1,430 | -33 |
| Ticketmaster live | 27 | 33 | -6 |
| Articles published | 857 of 952 | 857 of 952 | 0 |
| Sponsored videos live | 2 | 6 | -4 |

## Live events by region

| Region | Live events | Permanent places | One-time / multi-date | Ticketmaster | Kommuner with events | Kommuner |
|---|---:|---:|---:|---:|---:|---:|
| Stockholm | 423 | 319 | 104 | 26 | 26 | 26 |
| Västra Götaland | 169 | 169 | 0 | 0 | 48 | 49 |
| Skåne | 125 | 125 | 0 | 0 | 32 | 33 |
| Uppsala | 120 | 101 | 19 | 1 | 8 | 8 |
| Örebro | 101 | 101 | 0 | 0 | 12 | 12 |
| Östergötland | 81 | 81 | 0 | 0 | 13 | 13 |
| Kalmar | 64 | 64 | 0 | 0 | 12 | 12 |
| Dalarna | 63 | 63 | 0 | 0 | 15 | 15 |
| Jönköping | 61 | 61 | 0 | 0 | 13 | 13 |
| Västmanland | 57 | 57 | 0 | 0 | 10 | 10 |
| Gävleborg | 54 | 54 | 0 | 0 | 10 | 10 |
| Södermanland | 44 | 44 | 0 | 0 | 9 | 9 |
| Norrbotten | 7 | 7 | 0 | 0 | 6 | 14 |
| Värmland | 5 | 5 | 0 | 0 | 4 | 16 |
| Västerbotten | 5 | 5 | 0 | 0 | 3 | 15 |
| Blekinge | 4 | 4 | 0 | 0 | 3 | 5 |
| Jämtland | 4 | 4 | 0 | 0 | 3 | 8 |
| Västernorrland | 4 | 4 | 0 | 0 | 4 | 7 |
| Halland | 3 | 3 | 0 | 0 | 3 | 6 |
| Gotland | 2 | 2 | 0 | 0 | 1 | 1 |
| Kronoberg | 1 | 1 | 0 | 0 | 1 | 8 |
| **All Sweden** | **1,397** | **1,274** | **123** | **27** | **236** | **290** |

## What changed since 20 Oct

- Events -33: 30 one-time events ended; 3 permanent-place seasons ended (Bollnäs museum 30 Oct, Björköby djurpark 31 Oct,
  Järvsö Bergscykelpark 1 Nov). No new events were created after 18 Oct.
- Ticketmaster -6: Babblarna Täby, Mamma Mia, Anden i Glaset Uppsala, Harry Potter Del 1, Comic Con, Artist Alley.
- Sponsored -4: four question posts ended 31 Oct. Live: Alice i underlandet (to 5 Nov), Swedish House Maffia (to 31 Dec).

## Sheet updates done

- **Events tab:** 1,397 rows refreshed; 28/28 chunk hashes match; G23 and I292 = 1397; no leftover rows.
- **Ticketmaster tab:** F2 = 27. Rows 3, 11, 12, 16, 25, 26, 27 (ended) and 4 (Elvis, hidden on the app) marked red; G4 cleared
  so F2 skips the hidden Elvis show (its date is still in column D). No missing Ticketmaster events.
- **Sponsored tab:** 86 rows match the API (2 active, 84 expired); fixed 2 titles that had lost their first letter
  ("Älg & Vilt safari", "Östermalmsgatan").

## Open for the user

- The **Events_Update tab is gone** from the sheet (not hidden). Sources_Sweden's Stockholm, Uppsala and Total cells depend on it.
- Three seasonal places dropped off the app; they need next-season dates to come back.
- "Babblarna … Estrad Södertälje" sits on venue "Kulturskolan" in Tyresö, so it shows under Tyresö in the app.
