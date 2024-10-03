c, n = map(str, input().split())

n = int(n)

if c == 'A':
    for i in range(n):
        print(i+1, end=' ')
else:
    for i in range(n, 0, -1):
        print(i, end=' ')