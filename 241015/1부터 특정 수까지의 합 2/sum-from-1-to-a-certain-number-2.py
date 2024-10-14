def calc(n):
    if n == 1:
        return 1
    return calc(n-1) + n

N = int(input())

print(calc(N))