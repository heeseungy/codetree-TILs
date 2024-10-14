def star(n):
    for _ in range(n):
        print('*', end=' ')
    print()
    if n == 1:
        print('*')
        return
    star(n-1)
    for _ in range(n):
        print('*', end=' ')
    print()

n = int(input())

star(n)