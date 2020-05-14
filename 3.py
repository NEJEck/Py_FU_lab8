"""
Задание 3. Сортировка.
Отсортируйте данный массив, используя встроенную сортировку.
"""
n = int(input())
list_a = []
i = 0
while i != n:
    el = int(input())
    list_a.append(el)
    i += 1
list_a.reverse()
list_a.sort()
print(*list_a)
