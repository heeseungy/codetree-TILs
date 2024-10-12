n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(len(arr)):
    if cnt == 3:
        print(i)
        break
    if arr[i] == 2:
        cnt += 1