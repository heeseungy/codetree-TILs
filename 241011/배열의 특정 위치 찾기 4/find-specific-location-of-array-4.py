arr = list(map(int, input().split()))

cnt, val = 0, 0

for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        cnt += 1
        val += arr[i]

print(cnt, val)