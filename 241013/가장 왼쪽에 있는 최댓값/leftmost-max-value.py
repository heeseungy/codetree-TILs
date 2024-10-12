n = int(input())
nums = list(map(int, input().split()))

idx = len(nums)

while idx != 1:
    val = nums.index(max(nums))
    print(val + 1, end=' ')
    idx = val + 1
    nums = nums[:val]