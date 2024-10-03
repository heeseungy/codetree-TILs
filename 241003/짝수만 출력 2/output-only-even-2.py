a, b = map(int, input().split())

if a % 1 != 0:
    a += 1

while a >= b:
    print(a, end=' ')
    a -= 2