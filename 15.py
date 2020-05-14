"""
Задание 15. Семипроцентный барьер.
В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам. Каждый
избиратель указывает одну партию, за которую он отдает свой голос. В Государственную Думу попадают партии,
которые набрали не менее 7% от числа голосов избирателей. Дан список партий и список голосов избирателей. Выведите
список партий, которые попадут в Государственную Думу. """
fin = open("input15.txt", "r", encoding="utf8")
fout = open("output15.txt", "w", encoding="utf8")
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
for m in range(len(partwin)):
    if partwin[m] >= total:
        print(parties[m], file=fout)
fout.close()
