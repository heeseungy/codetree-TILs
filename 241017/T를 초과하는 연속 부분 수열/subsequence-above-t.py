n, t = map(int, input().split())
nums = list(map(int, input().split()))

max_length, current_length = 0, 0

for i in range(1, n):
    if nums[i] > t:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

print(max_length)