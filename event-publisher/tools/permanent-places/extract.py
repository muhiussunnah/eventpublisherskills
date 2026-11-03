import json, sys, collections, re
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
i = t.index('const EMBEDDED')
j = t.index('{', i)
# find the matching closing brace of the object literal
depth, k, ins, esc = 0, j, False, False
while True:
    ch = t[k]
    if ins:
        if esc: esc = False
        elif ch == '\\': esc = True
        elif ch == '"': ins = False
    else:
        if ch == '"': ins = True
        elif ch == '{': depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0: break
    k += 1
data = json.loads(t[j:k + 1])
places = data['places']
print('keys', list(data.keys()), 'places', len(places))
print('place keys', list(places[0].keys()))
reg = collections.Counter(p.get('region') for p in places)
print('regions', reg.most_common())
sel = [p for p in places if p.get('region') in ('Värmland', 'Halland')]
print('selected', len(sel))
mun = collections.Counter((p.get('region'), p.get('municipality')) for p in sel)
for (r, m), c in sorted(mun.items()):
    print(' ', r, '|', m, c)
json.dump(sel, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('sample', json.dumps(sel[0], ensure_ascii=False)[:1500])
