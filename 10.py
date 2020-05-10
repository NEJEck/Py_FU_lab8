from collections import defaultdict

total = defaultdict(list)
with open("input10.txt", "rt", encoding="utf-8") as f:
    for row in f:
        _class, range1 = map(int, row.rsplit(None, 2)[-2:])
        total[_class].append(range1)
print(*(max(total[k]) for k in sorted(total.keys())))
