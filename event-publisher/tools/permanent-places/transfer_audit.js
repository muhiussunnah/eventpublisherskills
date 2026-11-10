// Paste into the dashboard tab AFTER helpers.js (needs window.__P).
// 1) __expand(compact)  — turns the compact array written by compact.py back into publish specs.
//    Transfer: print the compact JSON in ~21 KB chunks, paste each as a template literal
//    (`__ca[k] = \`...\``), then verify a checksum before parsing:
//      cs(t) = sum(charCode(t[i]) * (i % 97 + 1)) mod 1000000007   (same formula in Python)
//    Compare cs(JSON.stringify(__expand(...))) with the Python value of the full specs
//    (childMinAge None -> 0, isFree -> bool) — equal means byte-identical specs.
// 2) __auditPublished(specs, done) — re-reads every published event + venue and compares field by field.
// 3) __buildEventsTSV() — rows for the sheet's Events tab (published live events only).
(() => {
  const WS = 'https://wsrv.nl/?url=', STD = '&w=1080&h=1080&fit=cover&output=jpg&q=88',
    LSTD = '&w=512&h=512&fit=contain&cbg=white&bg=white&output=jpg&q=90';
  // same as Python urllib.parse.quote(url, safe='')
  const q = (u) => encodeURIComponent(u).replace(/[!'()*]/g, (c) => '%' + c.charCodeAt(0).toString(16).toUpperCase());
  const hrs = (s) => s ? s.split(' ').map((h) => ({ day: +h[0], open: h.slice(1, 3) + ':' + h.slice(3, 5), close: h.slice(5, 7) + ':' + h.slice(7, 9) })) : null;
  window.__cs = (t) => { let s = 0; for (let i = 0; i < t.length; i++) s = (s + t.charCodeAt(i) * (i % 97 + 1)) % 1000000007; return s; };
  window.__expand = (C) => C.map(([key, o, v, e, im]) => ({
    key,
    org: { name: o[0], reuseId: o[1], isGovernment: !!o[2], email: o[3], phone: o[4], website: o[5], instagram: o[6], facebook: o[7], youtube: o[8],
      logoUrl: o[9] ? WS + q(o[9][0]) + (o[9][1] || LSTD) : null },
    venue: { title: v[0], address: v[1], lat: v[2], lng: v[3], municipality: v[4], website: v[5], email: v[6], phone: v[7], instagram: v[8], facebook: v[9],
      youtube: v[10], openingHours: hrs(v[11]), interestId: v[12], description: e[1], ctaLink: v[13] },
    event: { title: e[0], description: e[1], isFree: !!e[2], childMinAge: e[3],
      recurrence: { days: [...e[4][0]].map(Number), startTime: e[4][1] + ':00', durationMinutes: e[4][2], startDate: e[4][3], endDate: e[4][4] },
      interestIds: e[5], ctaLink: e[6] },
    img: { event: WS + q(im[0]) + (im[1] || STD), venue: WS + q(im[2]) + (im[3] || STD) },
  }));

  window.__auditPublished = async (specs, done) => {
    const byKey = Object.fromEntries(specs.map((s) => [s.key, s])); const out = [];
    for (const d of done.filter((x) => x.ok)) {
      const s = byKey[d.key]; const issues = [];
      const e = (await __P.api('GET', '/admin/events/' + d.ids.event)).j?.data;
      const p = (await __P.api('GET', '/admin/places/' + d.ids.place)).j?.data;
      if (!e) { out.push(d.key + ' NO EVENT'); continue; }
      if (e.title !== s.event.title) issues.push('title');
      if (e.description !== s.event.description) issues.push('desc');
      const r = e.recurrence || {}; const sr = s.event.recurrence;
      if (JSON.stringify([...(r.days || [])].sort()) !== JSON.stringify([...sr.days].sort())) issues.push('days');
      if ((r.startTime || '').slice(0, 5) !== sr.startTime.slice(0, 5)) issues.push('start');
      if (r.durationMinutes !== sr.durationMinutes) issues.push('duration');
      if (String(r.startDate).slice(0, 10) !== sr.startDate || String(r.endDate).slice(0, 10) !== sr.endDate) issues.push('dates');
      if (!!e.isFree !== !!s.event.isFree) issues.push('isFree');
      if (e.parentMinAge !== 18 || e.parentMaxAge !== 100 || e.childMaxAge !== 18 || e.childMinAge !== (s.event.childMinAge || 0)) issues.push('ages');
      if (!e.isRecurring) issues.push('notRecurring');
      if (!(e.images || []).length) issues.push('noImage');
      const ints = (e.interests || []).map((x) => x.interestId || x.id || x);
      if (JSON.stringify([...ints].sort()) !== JSON.stringify([...s.event.interestIds].sort())) issues.push('interests');
      if (e.place?.placeId !== d.ids.place) issues.push('place');
      if (!p) issues.push('noVenue'); else {
        if (p.isPublished !== true) issues.push('unpublished');
        if ((p.municipality?.name || p.municipality) !== s.venue.municipality) issues.push('kommun');
        if ((p.openingHours || []).length !== (s.venue.openingHours || []).length) issues.push('hours');
        if (p.owner?.organizationId !== d.ids.org) issues.push('org');          // organizer is `owner` on a place
        if (s.org.logoUrl && !p.owner?.avatar) issues.push('noLogo');
      }
      out.push(d.key + ' ' + d.ids.event + ' ' + (issues.join(', ') || 'OK'));
    }
    return out;
  };

  // Events tab rows: A edit link, B kommun, C region, D last date (one time only), E Recurring / One time.
  // Sorted region -> city -> one time first -> date -> id. Run in the background and poll window.__evb.
  window.__buildEventsTSV = async () => {
    const munis = []; for (let p = 1; p < 20; p++) { const r = await __P.api('GET', `/admin/municipalities?limit=100&page=${p}`); const a = r.j.data.municipalities || []; munis.push(...a); if (a.length < 100) break; }
    const reg = Object.fromEntries(munis.map((m) => [m.name, m.region?.name]));
    const ev = []; for (let p = 1; p < 100; p++) { const r = await __P.api('GET', `/admin/events?isEnd=false&limit=100&page=${p}`); const a = r.j.data.events || []; ev.push(...a); if (a.length < 100) break; }
    const pub = ev.filter((e) => e.place?.isPublished === true); const rows = [];
    for (const e of pub) {
      const city = e.place.municipality?.name || ''; let last = '';
      if (!e.isRecurring) { const d = (await __P.api('GET', '/admin/events/' + e.eventId)).j?.data; const ds = (d?.dates || []).map((x) => String(x.endDate || x.startDate || '').slice(0, 10)).filter(Boolean).sort(); last = ds[ds.length - 1] || ''; }
      rows.push({ id: e.eventId, city, region: reg[city] || '', last, type: e.isRecurring ? 'Recurring' : 'One time' });
    }
    const coll = new Intl.Collator('sv');
    rows.sort((a, b) => coll.compare(a.region, b.region) || coll.compare(a.city, b.city) || (a.type === b.type ? 0 : (a.type === 'One time' ? -1 : 1)) || a.last.localeCompare(b.last) || a.id.localeCompare(b.id));
    window.__evRows = rows;
    window.__tsv = rows.map((r) => ['https://dashboard.fammap.app/events/edit/' + r.id, r.city, r.region, r.type === 'Recurring' ? '' : r.last, r.type].join('\t')).join('\n');
    return { all: ev.length, pub: pub.length, noRegion: rows.filter((r) => !r.region).length };
  };
  return 'transfer_audit ok';
})();
