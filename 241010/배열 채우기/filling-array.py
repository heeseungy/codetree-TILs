arr = list(map(int, input().split()))

arr.reverse()

for i in arr:
    if i == 0:
        continue
    print(i, end=' ')