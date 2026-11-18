import json, sys, math, collections
PP = sys.argv[1]
s = json.load(open(PP + 'sel.json', encoding='utf-8'))
EXIST = set(range(1, 23))  # items 1-22 are already in the app (same title + same coordinates)
cand = [p for p in s if p['i'] not in EXIST]
json.dump(cand, open(PP + 'cand.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
KEYS = ('i', 'id', 'name', 'municipality', 'region', 'category', 'ageMin', 'ageMax', 'description', 'contact', 'coordinates',
        'source', 'priceLevel', 'tags')
order = ['Gotland', 'Västernorrland', 'Jämtland', 'Västerbotten', 'Norrbotten']
g = 0
idx = {}
for r in order:
    L = [p for p in cand if p['region'] == r]
    cnt = collections.Counter(p['municipality'] for p in L)
    L.sort(key=lambda p: (-cnt[p['municipality']], p['municipality'], p['i']))
    n = math.ceil(len(L) / 8)
    size = math.ceil(len(L) / n)
    for k in range(n):
        g += 1
        chunk = L[k * size:(k + 1) * size]
        name = f'{g:02d}'
        json.dump([{kk: p.get(kk) for kk in KEYS} for p in chunk], open(PP + f'group_{name}.json', 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        idx[name] = [r, len(chunk), sorted(set(p['municipality'] for p in chunk)), [p['i'] for p in chunk]]
json.dump(idx, open(PP + 'groups_index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('cand', len(cand), 'groups', g)
for k, v in idx.items():
    print(k, v[0], v[1], ', '.join(v[2]), v[3])
