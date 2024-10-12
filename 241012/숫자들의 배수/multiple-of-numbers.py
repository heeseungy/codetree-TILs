n = int(input())

arr = list([n * i for i in range(1, 11)])


cnt = 0
for a in arr:
    if cnt == 2:
        break
    if a % 5 == 0:
        cnt += 1
    print(a, end=' ')