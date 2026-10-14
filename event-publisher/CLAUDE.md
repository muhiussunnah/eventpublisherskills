# Session Bootstrap — Event Publisher Agent

**Read FIRST before any Famies work, in this exact order:**

1. **`agent-memory-v4.9.md`** — Operational baseline. All non-negotiables, code patterns, recent learnings, city status, error fixes. This is the single source of truth for "how this agent thinks right now." **Section 22 has the 2026-06-30 updates (API date format, cMax=18 rule, sheet row mapping, token rotation, Nordic image guidance).**

2. **`LEARNING-LOG.md`** — Dated training log, newest first. Everything the user taught after 2026-06-30 (e.g. permanent places → organizer/venue/event, privacy rule, image upload prefixes) is here.

3. **`references/event-rules.md`** — Rule manual. Verify `## Rule #` header count == `rule_count` in SKILL.md (24; rule numbers are sparse up to #65).

4. **`SKILL.md`** — Skill metadata + Step 1-7 publish workflow + Permanent Places workflow.

5. **`references/technical-patterns.md`** — API schemas and code patterns (incl. "Permanent Places Publishing").

6. **`references/Agent_System_Prompt_v4_FINAL.md`** and **`references/TRAINING_MEMORY_v4_FINAL.md`** — historical context only.

## Why this order

`agent-memory-v4.9.md` captures EVERYTHING you learned across all sessions up to 2026-06-30: the strict rules the user keeps repeating (no image = no publish, no duplicates, push OFF, ctaLink direct event URL, etc.), every code pattern that works (`__publishCity` helper, session hash dedup, Soleil CMS image extraction, PATCH eventDateId quirk), error fixes from real failures (Babblarna search URL, Lidingö semantic duplicates, Parkteatern cross-city image collision), and the current city completion status (all 27 cities + Uppsala completed Round 5, total = 1259 live events). Read it before doing anything else — it will save the user from re-explaining what he's already explained dozens of times.

The rule manual (`event-rules.md`) is the full reference. Memory file is the operational distillation; `LEARNING-LOG.md` holds everything learned after it.

## User identity

**Famies** (chaos.and.lovefam@gmail.com), FamMap workspace admin. He speaks Banglish (Bengali in Latin script). Address him as **"bondhu"**. He values: thorough deep-dive coverage, one-by-one publishing (not batch-then-fix), strict rule adherence confirmed BEFORE publish.

## GitHub home

Repo: **https://github.com/muhiussunnah/eventpublisherskills** (public — never commit tokens, passwords, JWTs,
or private persons' contact details). On a new computer: `git clone` it, copy `event-publisher/` into
`<project>/.claude/skills/`, and open Claude Code in that project.

## End-of-session protocol (user's standing request, 2026-10-14)

Whatever the user teaches becomes part of the skill:
1. Add a dated entry to `LEARNING-LOG.md` (rules/preferences, technical learnings, mistakes + fixes, follow-ups).
2. Update the file the learning belongs in (`SKILL.md`, `references/technical-patterns.md`, `references/event-rules.md`, `references/image-rules.md`) and bump `skill_version` / `last_updated` in SKILL.md.
3. Save the task's final report next to the others (`<REGION/CITY>-…-FINAL-REPORT-<date>.md`).
4. Secret-scan, commit (`git -c safe.directory=* …`), and push to the GitHub repo above.
   Commit as `muhiussunnah <276623937+muhiussunnah@users.noreply.github.com>` (author AND committer) and add
   **no** AI attribution / Co-Authored-By lines — the user wants commits to look like they came straight from muhiussunnah.

## What to do first in a new session

1. Read the files above
2. Identify what the user is asking for in their first message
3. `TaskCreate` for it
4. Use the city setup boilerplate from `agent-memory-v4.8.md` §2.2
5. Begin work

**Don't re-derive patterns. Don't re-discover known issues. Don't re-explain rules back to the user.** The memory file exists exactly so a new session can pick up where the previous one left off.
