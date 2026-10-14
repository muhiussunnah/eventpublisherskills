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
