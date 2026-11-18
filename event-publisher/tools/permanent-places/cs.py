import sys
for p in sys.argv[1:]:
    t = open(p, encoding='utf-8').read()
    print(p.split('/')[-1], len(t), sum(ord(c) * (i % 97 + 1) for i, c in enumerate(t)) % 1000000007, 'ascii' if t.isascii() else 'NON-ASCII')
