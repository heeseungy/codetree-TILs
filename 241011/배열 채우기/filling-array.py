arr = list(map(int, input().split()))

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])
    else:
        result.reverse()
        break

print(*result)