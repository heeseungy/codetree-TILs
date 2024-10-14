def calc(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input().split())

print(calc(a, b, c))