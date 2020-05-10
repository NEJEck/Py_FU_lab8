def intersection(a, b):
    c = a & b
    return sorted(c, key=int)


list_a = set(input().split())
list_b = set(input().split())
d = intersection(list_a, list_b)
print(*d)
