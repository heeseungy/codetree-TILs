n = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(1, 1001):
    if nums.count(i) == 1:
        result.append(i)

if not result:
    print(-1)
else:
    print(max(result))