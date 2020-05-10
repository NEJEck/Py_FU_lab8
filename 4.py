size = int(input())
shop = list(map(int, input().split()))
new_size = size
count = 0
for i in shop:
    if i < new_size:
        continue
    else:
        new_size = i + 3
        count += 1
print(count)
