n = int(input())
nums = [int(input()) for _ in range(n)]

max_length = 1
current_length = 1

for i in range(1, n):
    if nums[i] > nums[i-1]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 1

print(max_length)