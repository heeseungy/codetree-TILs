n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()
    print()

for i in range(n):
    for j in range(1, n-i):
        print('*', end='')
    print()
    print()