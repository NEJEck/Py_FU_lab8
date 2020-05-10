def merger(a, b):
    new_list = []
    d = a + b
    while d:
        delete_num = min(d)
        while delete_num in d:
            new_list.append(delete_num)
            d.remove(delete_num)
    return new_list


list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_c = merger(list_a, list_b)
print(list_c)
