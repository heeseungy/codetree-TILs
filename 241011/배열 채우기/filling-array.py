arr = list(map(int, input().split()))

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])
    else:
        break

result.reverse()
print(*result)