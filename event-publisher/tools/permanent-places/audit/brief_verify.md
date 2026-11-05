# Verification brief — is this published "permanent place" still correct?

You get a JSON file with ~N places that are published in a Swedish family app as recurring "always on" events.
A real museum just complained that the app showed it as open although the building has been closed for renovation
since 2018 and reopens late 2027. We must find every other place with wrong information.

For EACH place in your input file, check the official sources (the place's own website / the municipality's page for
it; news articles from SVT, SR, local newspapers if the site is unclear). Use WebFetch first; if the page needs
JavaScript or WebFetch fails, use WebSearch with the place name + "stängt" / "öppettider" / "renovering" and read the
result pages. Do NOT guess. Do NOT rely on Google Maps/TripAdvisor/Airbnb listings as the only source.

Answer these questions per place:
1. **status** — one of: `OPEN` (open to the public now or in its normal season), `CLOSED_RENOVATION`,
   `CLOSED_PERMANENT`, `MOVED` (exists but at another address), `SEASON_ONLY` (open only part of the year and the
   published date span/days contradict that), `NOT_A_VISITOR_PLACE` (no drop-in public access: booking-only,
   private, office, lab …), `UNCLEAR` (could not verify; say what you tried).
2. **evidence** — the URL you used and a short quote (Swedish ok) that proves the status / hours.
3. **reopen** — reopening date or season if closed (null if unknown).
4. **hours_conflict** — the published recurrence is in `rec` (days 0=Sun…6=Sat, startTime, durationMinutes,
   startDate–endDate). Set `true` if the place is closed on one of the published days, or the published window lies
   outside the official hours, or the official season ends before `endDate` / starts after `startDate`.
   Give `official_hours` as a short text ("Tis–sön 11–17, mån stängt; sommar dagligen 10–18").
5. **desc_wrong** — anything in the app description (`desc`) that contradicts the official source (wrong address,
   wrong "öppet …" days, wrong price claims, a feature that no longer exists). Quote it. Else null.
6. **isfree_wrong** — the app says `isFree` (true/false); set `true` if the official source contradicts it.
7. **action** — `keep`, `unpublish` (closed / not a visitor place / cannot be verified at all), `fix_hours`,
   `fix_desc`, `fix_free` (combine with `+`, e.g. `fix_hours+fix_desc`).
8. **confidence** — `high` (official page states it), `medium` (news/other reliable), `low`.

Write your result as a JSON array to the output path given in your prompt, one object per input place with keys:
`id, place, status, evidence_url, evidence_quote, reopen, hours_conflict, official_hours, desc_wrong, isfree_wrong,
action, confidence, note`. Write the file incrementally (after every 3 places) so nothing is lost if you are cut off.
Keep `note` short. Do not publish, edit or delete anything in any app — research only.
