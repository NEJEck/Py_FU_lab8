"""
Задание 8. Отсортировать список участников по алфавиту.
Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8. Например, для чтения откройте
файл с помощью open('input.txt', 'r', encoding='utf8'). """
from collections import namedtuple

Participant = namedtuple("Participant", "lastName firstName school score")


def main():
    with open("input8.txt", encoding='utf-8') as fin, open("output8.txt", "w") as fout:
        participants = [Participant(*i.split()) for i in fin]
        participants.sort(key=lambda x: x.lastName)
        print(*map(" ".join, participants), sep="\n", file=fout)


if __name__ == "__main__":
    main()
