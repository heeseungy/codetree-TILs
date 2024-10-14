n = int(input())
arr = [0] * 201

for _ in range(n):
    start, end = map(int, input().split())
    start += 100
    end += 100
    for i in range(start, end):
        arr[i] += 1

print(max(arr))