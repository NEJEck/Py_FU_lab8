"""
Задание 16. Упорядочить список партий по числу голосов.
Формат входных данных аналогичен предыдущей задаче. Выведите список всех партий, участвовавших в выборах,
отсортировав его в порядке убывания количества голосов избирателей, а при равном количестве голосов - в
лексикографическом порядке. """
fin = open("input16.txt", "r", encoding="utf8")
fout = open("output16.txt", "w", encoding="utf8")
reader = fin.readlines()
parties = []
vote = []
votes = 0
for i in reader:
    if i == 'VOTES:\n':
        votes = 1
    if votes == 0:
        parties.append(i)
    else:
        vote.append(i)
parties.pop(0)
vote.pop(0)
parties = [line.rstrip() for line in parties]
vote = [line.rstrip() for line in vote]
partwin = [0] * len(parties)
total = 0
for j in range(len(parties)):
    for k in range(len(vote)):
        if parties[j] == vote[k]:
            partwin[j] += 1
            total += 1
total *= 0.07
items = dict()
for m in range(len(partwin)):
    if partwin[m] >= total:
        if parties[m] not in items:
            items[parties[m]] = partwin[m]
for k in sorted(items, key=items.get, reverse=True):
    print(k, items[k], file=fout)
fout.close()
