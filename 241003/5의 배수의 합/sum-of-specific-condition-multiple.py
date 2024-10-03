a, b = map(int, input().split())

min_val = min(a, b)
max_val = max(a, b)

sum_val = 0

for i in range(min_val, max_val+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)