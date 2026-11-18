"""Collect the outcome of every place of the run: published (from the batch spec files) or skipped (+ reason).
usage: python -I -X utf8 outcome.py [ids.json]
Writes pp3/outcome.json: [{i, region, kommun, name, status, reason?, key?, title?, window?, period?, free?, copied?, eventId?}]
"""
import json, glob, sys, os, re
PP = '<scratchpad>/pp/'  # point at the current session's scratchpad folder
DN = ['sön', 'mån', 'tis', 'ons', 'tor', 'fre', 'lör']
sel = {p['i']: p for p in json.load(open(PP + 'sel.json', encoding='utf-8'))}
choice = json.load(open(PP + 'choice.json', encoding='utf-8'))
ids = json.load(open(sys.argv[1], encoding='utf-8')) if len(sys.argv) > 1 else {}

specs = {}
for f in sorted(glob.glob(PP + 'batch*.json')) + sorted(glob.glob(PP + 'local_*.json')) + sorted(glob.glob(PP + 'regen*.json')):
    for s in json.load(open(f, encoding='utf-8')):
        specs[s['key']] = s            # later files win (re-generated specs)

res = {}
grp = {}
for f in sorted(glob.glob(PP + 'res_*.json')):
    g = re.search(r'res_(\d+)\.json', f).group(1)
    for x in json.load(open(f, encoding='utf-8')):
        res[x['i']] = x
        grp[x['i']] = g


def window(r):
    d = sorted(r['days'], key=lambda k: (k - 1) % 7)
    if r['startTime'][:5] == '00:00' and r['durationMinutes'] >= 1439:
        return 'alltid öppet'
    h, m = map(int, r['startTime'].split(':')[:2])
    e = h * 60 + m + r['durationMinutes']
    days = 'alla dagar' if len(d) == 7 else ', '.join(DN[k] for k in d)
    return f"{days} {h:02d}:{m:02d}–{e // 60:02d}:{e % 60:02d}"


out = []
for i, x in sorted(res.items()):
    base = sel.get(i) or sel.get(i - 1000) or {}
    row = {'i': i, 'region': base.get('region'), 'kommun': base.get('municipality'), 'name': x.get('name') or base.get('name')}
    key = f"{grp[i]}-{i}"
    c = choice.get(str(i), {})
    if key in specs:
        s = specs[key]
        r = s['event']['recurrence']
        row.update(status='published', key=key, title=s['venue']['title'], window=window(r), period=f"{r['startDate']} → {r['endDate']}",
                   free=bool(s['event']['isFree']), copied='seasonCopied' in (x.get('flags') or []), start=r['startDate'], end=r['endDate'])
        if key in ids:
            row['eventId'] = ids[key][2] if isinstance(ids[key], list) else ids[key]
        else:
            row['status'] = 'NOT-CONFIRMED'
    else:
        row.update(status='skipped', reason=c.get('skip') or x.get('skip') or c.get('hold') or 'not accepted (validation problems)')
    out.append(row)
for i, p in sel.items():
    if i not in res and i <= 22:
        out.append({'i': i, 'region': p['region'], 'kommun': p['municipality'], 'name': p['name'], 'status': 'existing'})
    elif i not in res:
        out.append({'i': i, 'region': p['region'], 'kommun': p['municipality'], 'name': p['name'], 'status': 'MISSING'})
json.dump(out, open(PP + 'outcome.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
import collections
cnt = collections.Counter((r['region'], r['status']) for r in out)
for k in sorted(cnt, key=str):
    print(k, cnt[k])
print('total', len(out), collections.Counter(r['status'] for r in out))
print('specs', len(specs), 'ids', len(ids), 'spec keys without res', [k for k in specs if int(k.split('-')[1]) not in res])
