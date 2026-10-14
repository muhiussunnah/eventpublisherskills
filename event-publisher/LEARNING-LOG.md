# Learning Log — Event Publisher Agent

This is the running training file. **Every session ends by adding a dated entry here** with what the user taught,
what went wrong and how it was fixed, and which skill files were updated. Newest entry on top.
Then commit and push to https://github.com/muhiussunnah/eventpublisherskills so any computer can pull the latest.

Entry template:

```
## YYYY-MM-DD — <task>
**User asked:** …
**New rules / preferences from the user:** …
**What I learned (technical):** …
**Mistakes + fixes:** …
**Files updated:** …
**Open follow-ups:** …
```

---

## 2026-10-14 — Live events overview in the "Events" tab (gid 1719318267)
**User asked:** fill the Events tab with every live event only (expired ones fully removed): Edited Link, City, Region,
Expired Date, Type; plus Region → amount (21 regions) and City → amount (290 kommuner).
**New rules / preferences from the user:**
- Type = "Recurring" for recurring places (they never expire → Expired Date left empty).
- Type = "One time" for single-date AND multi-date events; Expired Date = the LAST date.
- Only live events in the list; region and city counts next to it.
**Result:** 1434 live events (193 one time, of which 72 multi-date; 1241 recurring), rows A2:E1435 sorted region → city →
one time first → date. F/G: 21 regions + Total (=1434); H/I: 290 cities + Total (=1434); 231 cities have events, 59 have 0.
Counts are formulas that ignore expired one-time rows automatically:
`=COUNTIFS(C$2:C;F2;D$2:D;"")+COUNTIFS(C$2:C;F2;D$2:D;">="&TODAY())` (same with column B for cities).
**What I learned (technical):**
- `GET /admin/events?isEnd=false` = live list (`data.totalEvents`); its `lastDate` is null for many one-time events → use `GET /admin/events/{id}` `dates[]` and take the max endDate.
- Municipality → region via `/admin/municipalities` (290 kommuner, 21 regions, names unique).
- Bulk data from the browser into my context: render it in a `<pre>` on the dashboard tab and call `get_page_text` (max 50 000 chars per call).
- Bulk write into Sheets with 100% accuracy (no hand-copying 18-digit IDs): put the TSV in a `<pre>`, select it with a Range, `ctrl+c` in that tab, then in Sheets jump to A2 and **`ctrl+shift+v`** (plain text — a normal ctrl+v of copied HTML puts every line in column A). Back up the user's clipboard first (PowerShell + System.Windows.Forms.Clipboard, text or image) and restore it right after.
- Pasting past row 1000 adds rows automatically.
**Mistakes + fixes:** first paste was ctrl+v (HTML) → all in column A → ctrl+z, re-pasted with ctrl+shift+v; F23 "Total" label did not land → typed it.
**Open follow-ups:** the list is a snapshot — re-run weekly so expired one-time rows disappear (counts already exclude them).

## 2026-10-14 — Sponsored posts list in the Weekly_Events_Update sheet
**User asked:** list every sponsored post from dashboard.fammap.app/sponsored (title + expired date) in the sheet tab
"Sponsored" (gid 301227144): active ones on top, expired ones below in order, and a side column that shows the active
count automatically.
**Result:** 86 posts (6 active, 80 expired). Columns: `#`, `Title`, `Expired Date`, `Status` (`=IF(C2>NOW();"Active";"Expired")`),
side block F: Total Active `=COUNTIF(C2:C87;">"&NOW())`, Total Expired, Total Sponsored. Active sorted by soonest
expiry, expired sorted newest → oldest.
**What I learned (technical):**
- API: `GET /admin/sponsored?page=1&limit=100[&isEnd=false|true]` → `data.sponsored[]` {sponsoredId, title, image, startDate, endDate, owner, municipality}, `data.totalSponsored`. `isEnd` matches the dashboard's active/expired split (endDate "YYYY-MM-DD 00:00:00").
- The sheet uses a Swedish locale → formula separators are `;`, ISO dates parse fine.
- No Google Sheets connector in this setup; writing into the user's sheet via Chrome works like this:
  Name Box (≈ x47,y113) → type `B1\n` → type the whole column joined with `\n` (Enter moves down). Formulas: type once, then select the range in the Name Box and `ctrl+d`.
- Do NOT: dispatch a synthetic `paste` event into Sheets (it crashes the editor: "An error occurred"); call `navigator.clipboard.writeText` from the page (hangs the renderer); use the OS clipboard (`Set-Clipboard` + ctrl+v) — it races with the user's own copying and once pasted the user's screenshot instead (undone with ctrl+z). Python on Windows writes `\r\n`; an extra `\r` makes Sheets insert blank rows.
- An emoji as the FIRST character of a typed cell gets dropped (starting edit mode swallows it); fix with F2 → Home → type emoji → Enter.
**Mistakes + fixes:** blank rows from `\r\r\n` (undone); user's clipboard image pasted (undone); leading emojis dropped on 3 titles (re-added).
**Open follow-ups:** the sorting is static — new sponsored posts need a re-run; Status and counts update by themselves.

## 2026-10-14 — GitHub home for the skill
**User asked:** push the whole folder to https://github.com/muhiussunnah/eventpublisherskills so it can be downloaded
on any computer, and keep writing every new learning into the skill files.
**New rules / preferences from the user:**
- After every session: add an entry here, update the relevant skill file(s), commit and push to the repo above.
**Files updated:** `CLAUDE.md` (bootstrap + end-of-session protocol), `README.md` (new repo URL, setup on a new computer),
`SKILL.md` (v1.37.0), this log. The `eventscounter` skill was added to the repo as `eventscounter/`.

## 2026-10-13 — Gävleborg permanent places (62 → 52 published)
**User asked:** publish the permanent places from the "Vad ska vi hitta på idag" HTML for Gävleborg as
organizer → venue → event; only if unique (nothing already in the app); real images from the places' own
websites/socials that fit the Famies family audience; collect as much organizer info as possible, 100% accurate.
**New rules / preferences from the user:**
- Order per place: organizer first, then venue, then event.
- Organizer = as much verified info as possible (legal/official name, phone, email, website, Instagram, Facebook, YouTube, logo).
- Images must be of the real place (official site / visit-site / socials), kids-and-parents friendly, no text.
- Check duplicates against the whole app before publishing; the input list can also contain duplicates.
**What I learned (technical):**
- `/admin/image` works with file-name prefixes `event.jpg-<ts>`, `place.jpg-<ts>`, `organization.jpg`, `campaign.jpg-<ts>` (the old "Folder name is not allowed" error is about the prefix).
- Organizer email is unique in the DB (error code 23505); state museums use their own org name.
- Place/org/event create schemas taken from the dashboard bundle — see technical-patterns.md "Permanent Places Publishing".
- `parentMaxAge` default is 100 (not 18).
- Recurrence must be a window open on every listed day; venue keeps the full per-day hours.
- Research in parallel subagents → JSON + image candidates → visual square-crop review → publish one by one → full audit.
**Mistakes + fixes:**
- Transparent logo became black → wsrv `bg=white`; PATCHed the avatar.
- Several agent recurrences overstated weekend hours (Aquarena, Fjärran, Länsmuseet, DOME, Färila, Hudik bad, Växbo Lin, Bollnäs museum, Parkbadet, Kungsberget) → fixed before publish.
- An org POST with a personal-name email was blocked by the auto-mode classifier → dropped personal contacts (new privacy rule).
- O'Learys "Gävle" bowling photo was really a chain photo already used on O'Learys Uppsala → used a different official photo.
**Skipped (with reasons in the report):** Göransson Arena, Alfta simhall, Världens största skidor, Hudiksvalls Teater, Ljusne inomhusbad.
**Files updated:** `GAVLEBORG-PERMANENT-PLACES-FINAL-REPORT-2026-10-13.md`, `SKILL.md` (Permanent Places section),
`references/technical-patterns.md` (Permanent Places Publishing).
**Open follow-ups:** extend Bollnäs museum (ends 30 Oct), Bergscykelpark (1 Nov), Trolska Skogen (20 Dec) when new
periods are announced; replace copied 2027 season spans when official dates come out; Statens fastighetsverk org has
isGovernment false + Hagaparken website; Jönköping batch uses parentMaxAge 18.
