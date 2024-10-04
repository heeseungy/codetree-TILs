n = int(input())

num = 1

for i in range(n):
    for j in range(num):
        print('*', end='')
    num += 2
    print()