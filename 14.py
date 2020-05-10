tariffs = sorted([int(s) for s in input().split()])
distances = sorted([int(s) for s in input().split()], reverse=True)
print(sum(t*d for t, d in zip(tariffs, distances)))
