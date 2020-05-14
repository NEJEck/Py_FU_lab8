"""
Задание 13. Проходной балл.
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ, каждый из них оценивается
целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по
любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
В конкурсе участвует N человек, при этом количество мест равно K. Определите проходной балл, то есть такое количество
баллов, что количество участников, набравших столько или больше баллов не превосходит K, а при добавлении к ним
абитуриентов, набравших наибольшее количество баллов среди непринятых абитуриентов, общее число принятых абитуриентов
станет больше K. """
myFile = open("input13.txt", "r", encoding="utf8")
k = int(myFile.readline())
myList = []
for line in myFile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        myList.append(newLine)
myFile.close()
myList.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
myList.reverse()
konk = []
for i in myList:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(sum)
n = len(konk)


def konkurs(n, k, konk):
    if n <= k:
        return 0
    elif konk[k] == konk[0]:
        return 1
    for i in range(k, 0, -1):
        if konk[i] < konk[i - 1]:
            return konk[i - 1]


print(konkurs(n, k, konk))
