n, k = map(int, input().split())
arr = [0] * n

for _ in range(k):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        arr[i] += 1

print(max(arr))