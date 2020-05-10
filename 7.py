with open("input7.txt", "rt", encoding="utf-8") as f:
    items = dict()
    counter9 = 0
    counter10 = 0
    counter11 = 0
    my_lines = f.readlines()
    for i in my_lines:
        item = list(map(str, i.split()))
        if item[2] == '9':
            counter9 += 1
        elif item[2] == '10':
            counter10 += 1
        elif item[2] == '11':
            counter11 += 1
        if item[2] not in items:
            items[item[2]] = int(item[3])
        else:
            items[item[2]] += int(item[3])
if '9' in items:
    print(int(items['9']) / counter9, end=' ')
if '10' in items:
    print(int(items['10']) / counter10, end=' ')
if '11' in items:
    print(int(items['11']) / counter11, end=' ')
