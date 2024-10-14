def calc(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return int(total/10)

N = int(input())

print(calc(N))