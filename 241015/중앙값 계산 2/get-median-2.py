n = int(input())
nums = list(map(int, input().split()))

center = []
for i in range(len(nums)):
    center.append(nums[i])
    if i % 2 == 0:
        center.sort()
        print(center[len(center)//2], end=' ')