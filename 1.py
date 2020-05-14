"""
Задание 1. Слияние списков.
Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный список С (то
есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B), возвращающей новый
список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные списки запрещается. Использовать
функцию sorted и метод sort запрещается. """


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
