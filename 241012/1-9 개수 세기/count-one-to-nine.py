n = int(input())
arr = list(map(int, input().split()))

count = [0 for _ in range(9)]

for a in arr:
    count[a-1] += 1

for c in count:
    print(c)