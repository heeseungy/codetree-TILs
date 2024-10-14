N = int(input())
nums = list(map(int, input().split()))

nums.sort()
max_group_sum = 0

for i in range(N):
    group_sum = nums[i] + nums[2*N-1-i]
    # 최댓값 갱신
    max_group_sum = max(max_group_sum, group_sum)
    
print(max_group_sum)