n = int(input())
nums = list(map(int, input().split()))

idx, val = 0, 0

for i in range(len(nums)):
    if nums.count(i) == 1:
        if nums[i] > val:
            val = nums[i]
            idx = i

if val == 0:
    print(-1)
else:
    print(idx)