def CountSort(list1):
    sortedlist = [0] * 101
    for i in list1:
        sortedlist[i] += 1
    for i in range(101):
        print((str(i) + ' ') * sortedlist[i], end='')


list1 = [int(i) for i in input().split()]
CountSort(list1)


