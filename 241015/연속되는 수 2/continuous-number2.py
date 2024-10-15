n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

cnt = 1
max_cnt = 1
for i in range(1, n):
    if arr[i] == arr[i-1]:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 1

print(max_cnt)