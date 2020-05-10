with open("input12.txt", "rt", encoding="utf-8") as f:
    items = dict()
    counter9 = 0
    max9 = 0
    counter10 = 0
    max10 = 0
    counter11 = 0
    max11 = 0
    my_lines = f.readlines()
    for i in my_lines:
        item = list(map(str, i.split()))
        if item[2] == '9':
            if int(item[3]) > max9:
                max9 = int(item[3])
                counter9 = 1
            elif int(item[3]) == max9:
                counter9 += 1
        if item[2] == '10':
            if int(item[3]) > max10:
                max10 = int(item[3])
                counter10 = 1
            elif int(item[3]) == max10:
                counter10 += 1
        if item[2] == '11':
            if int(item[3]) > max11:
                max11 = int(item[3])
                counter11 = 1
            elif int(item[3]) == max11:
                counter11 += 1
print(counter9, counter10, counter11, sep=' ')

