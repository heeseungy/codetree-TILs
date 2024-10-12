arr = list(map(int, input().split()))

flag = 0

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

# print(arr)

for a in arr:
    if a % 2 == 1:
        print(a + 3, end=' ')
    else:
        print(a // 2, end=' ')