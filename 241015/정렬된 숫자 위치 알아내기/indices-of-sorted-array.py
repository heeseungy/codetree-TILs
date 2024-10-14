n = int(input())
nums = list(map(int, input().split()))

idx_nums = [(val, idx) for idx, val in enumerate(nums)]

idx_nums.sort()

position = [0] * n
for new_idx, (val, origin_idx) in enumerate(idx_nums):
    position[origin_idx] = new_idx + 1

print(*position)