# Fix brief — build the corrected data for published permanent places

Today is 2026-11-05. Each input item is a place that is live in a Swedish family app as a recurring event, and that
an audit found wrong (hours, season, price flag or description). The audit result is included (`audit.*`). Your job
is to produce the exact corrected values. Accuracy matters more than speed: only facts from the official source.

## Sources
Use `audit.evidence_url`, `audit.official_hours`, `audit.evidence_quote`, `audit.note` first. If they do not give
the hours for every weekday, the season dates, or the price, WebFetch the official page (the evidence URL, the
place's website and its öppettider / besök / priser subpages, or the kommun page). Use at most 5 WebSearch calls in
total (the quota is shared). No browser tools, no reader/proxy services, no edits anywhere, no publishing.

## Output (JSON array, one object per input item, written with the Write tool every 3 items)
```
{
 "id": "<event id>",
 "decision": "patch" | "hide" | "no_change",
 "hide_reason": null | "short reason",
 "hours_by_day": {"0": "HH:MM-HH:MM" | null, "1": ..., ..., "6": ...},
 "season": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "basis": "official" | "copied_2026_pattern" | "year_round"},
 "recurrence": {"days": [..], "startTime": "HH:MM:SS", "durationMinutes": N, "startDate": "YYYY-MM-DD", "endDate": "YYYY-MM-DD"} | null,
 "isFree": true | false,
 "description": null | "<new Swedish description>",
 "title": null | "<corrected title>",
 "ctaLink": null | "<corrected official URL>",
 "evidence_url": "<URL you used>",
 "note": "<short: what changed and why>"
}
```
- `hours_by_day`: day 0 = Sunday … 6 = Saturday. The official public opening hours that apply during the span you
  publish (`null` = closed that day). Several ranges: `"10:00-12:00,13:00-16:00"`. For swimming pools use the hours
  for public/family swimming (allmänhetens bad, familjebad, äventyrsbad), not lap swim, morning swim, school or
  club time. For outdoor places that are always open: `"00:00-23:59"` every day.
- `recurrence` is the ONE weekly time window the app shows. Rules:
  1. The window [startTime, startTime + durationMinutes] must lie inside the open hours on EVERY day in `days`.
  2. Choose the window and the set of days that cover the most of the real opening time; drop days whose hours
     cannot share the window. Keep at least 2 hours if possible. Weekend days are valuable for families.
  3. `startDate` = 2026-11-05, or the first open date if the place is closed now (season start / reopening date).
     `endDate` = end of the season or period, at most 2027-12-31. Never an `endDate` before 2026-11-05.
  4. Seasonal place whose next season dates are not published yet: copy the 2026 season dates into 2027 and set
     `season.basis` = "copied_2026_pattern".
  5. Hours that differ between periods (winter/summer, term/holiday): use a window that fits both periods if it
     keeps ≥ 2 hours; otherwise publish only the current/next period, end `endDate` at its last day, and say so in
     `note`.
  5b. If a short closure (under 6 weeks, e.g. maintenance or renovation) splits the span, publish the LONGER open
     period, not the first one, and mention the other period in `note`.
  6. Always-open outdoor place: days 0–6, "00:00:00", 1439.
  7. If the current recurrence is already correct, return it unchanged.
- `isFree`: `true` only if entry is free for everyone (free museum, library, park, nature reserve, beach, open
  monument, town). `false` if adults pay, even when children are free. Activities that cost money (bowling,
  climbing, play centres, go-kart, swimming) are `false`.
- `description`: rewrite only if the current text contradicts the official facts (wrong features, wrong address or
  area, "öppet dagligen", "fri entré" when it is paid, a closed part described as open, text about another place).
  Otherwise `null`. A rewrite is Swedish, 300–650 characters, plain prose in 3–5 sentences, written for families
  with children, only facts from the official source, no opening-hours lists, no prices other than "fri entré" when
  true, no markdown, no emojis. You may say "säsongsöppet sommartid" or "öppet året runt".
- `title`: only if the current title names the wrong place (e.g. a renamed venue). Format "Platsnamn – kort
  beskrivning" if you rewrite it, at most 110 characters.
- `ctaLink`: only if the current link is dead, a 404, or a spam/casino page. Give the official page instead.
- `decision: "hide"` when there are no regular drop-in hours at all (ticketed performances or screenings only,
  booking-only tours or rooms, by appointment only), when the place is closed with no known reopening date, or when
  you cannot confirm the place exists. Then `recurrence`, `description` may be null.
- `decision: "no_change"` only when, after checking, everything currently published is correct.

At the end, check that every input id is in the output exactly once, then reply with a short summary: counts per
decision and the ids you set to hide.
