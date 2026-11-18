import json, sys
PP = '<scratchpad>/pp/'  # point at the current session's scratchpad folder
c = json.load(open(PP + 'choice.json', encoding='utf-8'))
upd = json.loads(sys.argv[1])
for k, v in upd.items():
    c.setdefault(k, {}).update(v)
json.dump(c, open(PP + 'choice.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('choices', len(c), 'updated', len(upd))
