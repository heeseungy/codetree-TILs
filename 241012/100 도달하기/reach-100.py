n = int(input())

arr = [0 for _ in range(100)]
arr[0] = 1
arr[1] = n

print(*arr[:2], end=' ')

for i in range(2, len(arr)):
    arr[i] = arr[i-2] + arr[i-1]
    if arr[i] < 100:
        print(arr[i], end=' ')
    else:
        print(arr[i], end=' ')
        break