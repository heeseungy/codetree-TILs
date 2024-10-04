n = int(input())

flag = 0

for i in range(2, n):
    if n % i == 0:
        print('C')
        break
else:
    print('N')