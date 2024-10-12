nums = list(map(int, input().split()))
big, small = 0, 1000

for n in nums:
    if n > 500:
        if n < small:
            small = n
    else:
        if n > big:
            big = n

print(big, small)