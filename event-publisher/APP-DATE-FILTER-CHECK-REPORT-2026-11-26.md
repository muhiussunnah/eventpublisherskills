# App check: date + region filter for the published permanent places (2026-11-26)

Asked by the CEO: "Can you please check if the boys' date filter works in app? Where you publish all the permanent places…?"

## How it was tested
- Famies Android app, **Internal Beta 3.1.7 (590)**, on an Android 15 emulator, logged in with a normal user account, GPS set to Täby.
- Events tab → **Region** (county → areas) and the date chips **Today / Tomorrow / Weekend / Select date**.
- Every list was scrolled to the end, all cards were read out, and compared with what we published
  (`NORRLAND-GOTLAND-PERMANENT-PLACES-FINAL-REPORT-2026-11-18.md`: place, weekdays, period).

## Result

| Test | Should show | App shows | |
|---|---|---|---|
| Gotland, Today (Thu 26 Nov) | 8 | 8 | exact |
| Gotland, Mon 30 Nov | 6 | 6 | exact (the two Thu–Sun places are hidden) |
| Jämtland, Today (Thu 26 Nov) | 12 | 12 (+ the older Jamtli) | exact |
| Jämtland, Sat 19 Dec 2026 | 23 | 11 (+ Jamtli) | **12 ski resorts missing** |
| Gotland, Wed 7 Jul 2027 | 21 | only the 6 year-round places | **15 summer places missing** |
| Stockholm area, Mon 30 Nov | Monday-closed museums hidden | hidden (Millesgården, Naturhistoriska, Etnografiska …) | ok (spot check, list too long for an exact count) |

- **Works:** region/area filter, weekday logic and the date filter for every place whose period has already started.
- **Does not work:** recurring places whose period starts in the future (ski season from December 2026, summer 2027)
  are not shown anywhere: not in the unfiltered list, and not when a date inside their season is picked.
  103 of the 196 places published in Norrbotten, Västerbotten, Västernorrland, Jämtland and Gotland have a future start,
  so the app currently shows far fewer places than are published (Gotland: 26 live, 8 visible; Jämtland: 40 live, 13 visible).
- **Small:** with a date selected, the cards still say "Today" instead of the selected date.
- The beta build is dark only: no Appearance setting, and it ignores Android's light mode.

Checked in the dashboard on the same day: the missing places are published and live there (status `ongoing`, venue
published), e.g. the five example IDs below; the dashboard counts Gotland 26 and Jämtland 40 live.

## Message for the developers

**1. Recurring events with a future start date never appear in the app (high)**

- Build: Famies Android, Internal Beta 3.1.7 (590). Tested 26 Nov 2026.
- Steps: Events tab → Region → Jämtland (select all areas) → Select date → 19 Dec 2026 → Save.
- Expected: every published recurring event that is open on that day, 23 places, including the ski resorts whose
  recurrence starts 11–19 Dec (e.g. SkiStar Åre – Åre by `497412088340186818`, Lofsdalen `497418167639902145`,
  Vemdalsskalet `497416159491032938`).
- Actual: only the 11 places whose recurrence start date is already in the past. None of the 12 ski resorts.
- Same with Region → Gotland → 7 Jul 2027: expected 21, only the 6 year-round places are listed. The 15 summer places
  (e.g. Bergmancenter `497410260261176927`, Bungemuseet `497409895323174465`, period 1 Jun – 30/31 Aug 2027) are missing.
- With no date selected they are not listed as upcoming either, while one-time future events are (they show their date).
- What works: weekdays are handled correctly for started events (a Thursday-only place, `497417382029985694`, is hidden on
  a Saturday; Monday-closed museums are hidden on a Monday).
- Guess at the cause: the list query seems to require `recurrence.startDate <= today` for recurring events instead of
  checking the selected date (or "any upcoming date") against `startDate … endDate`.
- Impact: families cannot find seasonal places before the season starts (skiing at Christmas, summer 2027). 103 of the
  196 places published in the five northern regions + Gotland are affected right now, more in other regions.

**2. Card date label ignores the selected date (low)**

- Steps: Events tab → pick Tomorrow or any date with "Select date".
- Expected: the card shows the selected date (or the next opening on/after it), e.g. "Sat 19 Dec".
- Actual: recurring events always show "Today".
