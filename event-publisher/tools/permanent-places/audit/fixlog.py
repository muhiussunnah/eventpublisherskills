import json, collections, csv, os
AUD = r"C:\Users\User\AppData\Local\Temp\claude\793086065a500b32\4ad7473a-f7bd-4184-b47a-6ef00f11c16a\scratchpad\audit"
REPO = r"F:\eventpublisherskills\eventpublisherskills\event-publisher"
os.chdir(AUD)
det = json.load(open('det.json', encoding='utf-8-sig'))
rows = {r['id']: r for r in json.load(open('audit_results.json', encoding='utf-8'))}
hide1 = json.load(open('hide_list.json', encoding='utf-8'))
hide1['445118974879892668'] = 'duplicate of 442373224206992429 (VREX Bromma)'
fixh = {x['id']: x for x in json.load(open('fix_hides.json', encoding='utf-8'))}
hide2 = list(fixh.keys()) + ['442370036577896239', '442261399784162936']
hold = {"178316519871120801": "487837411036923252", "185717206598846112": "487837593019385205", "187991706086442842": "487837625768510838",
        "248678996634535313": "487837658643465591", "427718020366894381": "487837745398449528", "377312454805325496": "487837787492484473",
        "377371173417158342": "487837829443913082", "429867006406198753": "487837871420507515", "429887652028777506": "487837904035415420",
        "186703520404113140": "475592282393838746", "253228975550137400": "487837957194024317", "259199720268793095": "487837990085756286",
        "253319603671827571": "487838077453108607", "184929995582375506": "487838110328063360"}
moved = {'430215746082080383', '426615896685970906', '427970066991056881', '427332554987701781', '427785129532884205', '430201818467828795',
         '428077923988178894', '428036728733861616', '427739684425204780', '430224815786329285', '441184704121571018', '429877204319503616',
         '429917923310602044', '429259544997168761', '427315636918584592', '429352997781275743', '427962257054401786', '427293853205169174',
         '427278805409760720', '427034787606201642', '427086212767975421', '429400706152170893'}
already = {'436014765366609100', '445128704851477680', '441696271703508349'}
w1 = json.load(open('apply_w1.json', encoding='utf-8'))
w2 = json.load(open('apply_w2.json', encoding='utf-8'))
A = {x['id']: x for x in json.load(open('apply.json', encoding='utf-8'))}
w3ids = ['441726729573139942', '441712961082394053', '441678168147920186']
skip = {'442261399784162936', '445118974879892668', '442370036577896239'}
applied = list(w1) + [x for x in w2 if x['id'] not in skip] + [A[i] for i in w3ids]

def clean(s):
    return (s or '').replace('|', '/').replace('\n', ' ')

cnt = collections.Counter(k for x in applied for k in x['ov'])
L = ['# Permanent places — corrections applied (2026-11-05)\n',
     'Follow-up to `PERMANENT-PLACES-ACCURACY-AUDIT-2026-11-05.md`. The user approved all fixes. Every change is reversible; nothing was deleted.\n',
     '| | Count |', '|---|---|',
     f'| Events hidden (closed, booking/ticket-only, unverifiable, duplicates) | {len(hide1) + len(hide2)} |',
     f'| — first pass (audit verdicts + duplicate copies) | {len(hide1)} |',
     f'| — second pass (no regular drop-in hours or no published season, found while fixing) | {len(hide2)} |',
     f'| Events corrected | {len(applied)} |',
     f'| — recurrence (days, hours, season dates) | {cnt["recurrence"]} |',
     f'| — isFree | {cnt["isFree"]} |',
     f'| — description rewritten from the official source | {cnt["description"]} |',
     f'| — title | {cnt["title"]} |',
     f'| — ctaLink (dead, casino spam or missing) | {cnt["ctaLink"]} |',
     '| Events moved to their own correct venue | 6 |',
     '| Venue addresses / map pins / kommun corrected | 13 |',
     '| Published live events after the fixes | 1212 (was 1484) |\n',
     'Every corrected event also got `parentMaxAge: 100` where it had 18 or 99.\n',
     '## How hiding works (reversible)',
     '- Venue had no other events → venue `isPublished:false` (`PATCH /admin/places/{id}`). Re-publish: PATCH `isPublished:true`.',
     '- Venue shared with other events, or a general venue with past events → the event was moved to an unpublished holding venue `[Dold] <venue> – ej aktuell`. Re-publish: PATCH the event `placeId` back to the original venue.\n',
     '## Holding venues', '| Original venue | Holding venue |', '|---|---|']
for k, v in hold.items():
    L.append(f'| {k} | {v} |')
L += ['\n## Hidden events', '| Event ID | Place | Kommun | Original venue | Method | Reason |', '|---|---|---|---|---|---|']

def row(i, reason):
    d = det.get(i) or {}
    p = d.get('place') or {}
    if i in already:
        m = 'venue already unpublished 2026-10-19'
    elif i in moved:
        m = 'moved to holding ' + hold.get(p.get('id'), '?')
    else:
        m = 'venue unpublished'
    L.append(f"| {i} | {clean(p.get('title'))} | {clean(p.get('muni'))} | {p.get('id')} | {m} | {clean(reason)[:140]} |")

for i, r in hide1.items():
    if r.startswith('audit'):
        r = r + ' — ' + clean((rows.get(i) or {}).get('evidence_quote'))[:100]
    row(i, r)
for i in hide2:
    if i in fixh:
        r = fixh[i].get('reason') or ''
    elif i == '442370036577896239':
        r = 'duplicate of 430206808062199646 (Storkyrkan)'
    else:
        r = 'duplicate of 486683801863357590 (Hallands kulturhistoriska museum)'
    row(i, r)
L += ['\n## Events moved to their own venue', '| Event | New venue ID | Old venue ID |', '|---|---|---|']
for e, t, n, o in [('427749763002172961', "Leo's Lekland Barkarby", '487855164493956483', '184408384697566772'),
                   ('435898123416537027', "Leo's Lekland Borås", '487855198618813828', '184408384697566772'),
                   ('427308615494305301', "Leo's Lekland Täby/Arninge", '487855232768836997', '184408384697566772'),
                   ('430052341895431889', 'Klättercentret Telefonplan', '487855266826585478', '428032702118135789'),
                   ('430049351616726978', 'Klättercentret Akalla', '487855300699784583', '428032702118135789'),
                   ('427929194798810117', 'Drottningholms slott (existing venue reused)', '379548563769689140', '178316519871120801')]:
    L.append(f'| {e} {t} | {n} | {o} |')
L += ['\n## Corrected events', 'Full list with old and new values: `audits/permanent-places-fixes-2026-11-05.csv`.\n']
fu = json.load(open('followups.json', encoding='utf-8'))
L.append('## Follow-ups')
L.append('- Events whose published span ends before April 2027 because the next season or period is not published yet. Re-check and extend:')
for e, p, m, i in fu['soon']:
    if i in ('442261399784162936', '462624691236931541', '442254950060295586'):
        continue
    L.append(f'  - {e}: {p} ({m}), {i}')
L.append(f'- {len(fu["copied"])} seasonal events use the 2026 season dates copied into 2027 (`copied_2026_pattern`); confirm when the 2027 dates are out.')
L.append('- Some events the audit found correct (1 Oct 2026 batch) still have parentMaxAge 18; that bulk change was outside the approved fix list and was not made.')
open(os.path.join(REPO, 'PERMANENT-PLACES-FIXES-2026-11-05.md'), 'w', encoding='utf-8').write('\n'.join(L))
os.makedirs(os.path.join(REPO, 'audits'), exist_ok=True)
with open(os.path.join(REPO, 'audits', 'permanent-places-fixes-2026-11-05.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['eventId', 'place', 'kommun', 'old_days', 'old_start', 'old_minutes', 'old_startDate', 'old_endDate', 'old_isFree',
                'new_days', 'new_start', 'new_minutes', 'new_startDate', 'new_endDate', 'new_isFree', 'description_rewritten', 'new_title', 'new_ctaLink'])
    for x in applied:
        d = det[x['id']]
        r = d['rec'] or {}
        o = x['ov']
        n = o.get('recurrence') or {}
        w.writerow([x['id'], d['place']['title'], d['place']['muni'], ''.join(str(k) for k in sorted(r.get('days') or [])), r.get('startTime'),
                    r.get('durationMinutes'), r.get('startDate'), r.get('endDate'), d['isFree'],
                    ''.join(str(k) for k in sorted(n.get('days') or [])) if n else '', n.get('startTime', ''), n.get('durationMinutes', ''),
                    n.get('startDate', ''), n.get('endDate', ''), o.get('isFree', ''), 'yes' if o.get('description') else '',
                    o.get('title', ''), o.get('ctaLink', '')])
print('applied', len(applied), 'hidden', len(hide1) + len(hide2), dict(cnt))
