n = int(input())

arr = list(map(int, input().split()))
result = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        result.append(arr[i])

result.reverse()
print(*result)