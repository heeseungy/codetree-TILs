arr = list(map(int, input().split()))

num = 0
for i in range(len(arr)):
    if arr[i] == 0:
        num = i
        break

print(sum(arr[0:num]))