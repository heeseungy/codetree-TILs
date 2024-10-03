n = int(input())

sum_val = 1

for i in range(2, n):
    if n % i == 0:
        sum_val += i

if sum_val == n:
    print('P')
else:
    print('N')