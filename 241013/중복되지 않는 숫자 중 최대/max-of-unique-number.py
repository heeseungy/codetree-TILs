n = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(1, 1001):
    if nums.count(i) == 1:
        result.append(i)

print(max(result))