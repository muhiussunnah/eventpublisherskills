"""Write the final report of a permanent-places run from pp3/outcome.json.
usage: python -I -X utf8 mkreport.py <out.md> <head.md> <tail.md>
head.md / tail.md are hand-written parts (summary, checks / follow-up notes); this script adds the tables.
"""
import json, sys, collections
PP = '<scratchpad>/pp/'  # point at the current session's scratchpad folder
ORDER = ['Gotland', 'Västernorrland', 'Jämtland', 'Västerbotten', 'Norrbotten']
out = json.load(open(PP + 'outcome.json', encoding='utf-8'))
head = open(sys.argv[2], encoding='utf-8').read().rstrip() + '\n'
tail = open(sys.argv[3], encoding='utf-8').read().rstrip() + '\n'
key = lambda r: (ORDER.index(r['region']), r['kommun'], r.get('title') or r['name'])
pub = sorted([r for r in out if r['status'] == 'published'], key=key)
skip = sorted([r for r in out if r['status'] == 'skipped'], key=key)
exist = sorted([r for r in out if r['status'] == 'existing'], key=key)
assert not [r for r in out if r['status'] not in ('published', 'skipped', 'existing')]
L = [head]
L.append('## Per region\n| Region | In the file | Already in the app | Published now | Skipped |\n|---|---|---|---|---|')
for reg in ORDER:
    n = lambda st: sum(1 for r in out if r['region'] == reg and r['status'] == st)
    infile = sum(1 for r in out if r['region'] == reg and r['i'] < 1000)
    L.append(f"| {reg} | {infile} | {n('existing')} | **{n('published')}** | {n('skipped')} |")
L.append(f"| **Total** | {sum(1 for r in out if r['i'] < 1000)} | {len(exist)} | **{len(pub)}** | {len(skip)} |\n")
L.append('## Published places\n| Region | Kommun | Place | Event window | Period | Free | Season | Event ID |\n|---|---|---|---|---|---|---|---|')
for r in pub:
    L.append(f"| {r['region']} | {r['kommun']} | {r['title'].replace('|', '/')} | {r['window']} | {r['period']} | {'ja' if r['free'] else 'nej'} | "
             f"{'kopierad 2026' if r['copied'] else ''} | {r['eventId']} |")
L.append('\n## Skipped places\n| Region | Kommun | Place | Reason |\n|---|---|---|---|')
for r in skip:
    reason = ' '.join(str(r['reason']).replace('|', '/').split())
    if len(reason) > 230:
        reason = reason[:227] + '…'
    L.append(f"| {r['region']} | {r['kommun']} | {r['name'].replace('|', '/')} | {reason} |")
L.append('\n## Follow-ups')
L.append('- Seasonal places with the last season copied into 2027 — confirm when the official 2027 dates are published:')
for r in pub:
    if r['copied']:
        L.append(f"  - {r['title']} ({r['kommun']}): {r['period']}")
short = [r for r in pub if r['end'] < '2027-04-01']
L.append('- Events that end before April 2027 (hours published only that far, or a short winter season) — extend when new hours appear:')
for r in sorted(short, key=lambda r: r['end']):
    L.append(f"  - {r['title']} ({r['kommun']}): ends {r['end']}")
L.append(tail)
open(sys.argv[1], 'w', encoding='utf-8', newline='\n').write('\n'.join(L))
print('published', len(pub), 'skipped', len(skip), 'existing', len(exist), 'copied', sum(1 for r in pub if r['copied']), 'short', len(short))
c = collections.Counter()
for r in skip:
    t = str(r['reason']).lower()
    k = ('booking' if 'book' in t else 'no hours/season' if ('no published' in t or 'hours' in t or 'season' in t) else 'photo' if 'photo' in t or 'image' in t
         else 'duplicate' if 'duplicate' in t else 'closed' if 'closed' in t or 'stängt' in t else 'other')
    c[k] += 1
print(dict(c))
