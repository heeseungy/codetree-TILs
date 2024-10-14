def odd(n):
    if n == 0:
        return
    odd(n-1)
    print(n, end=' ')

def even(n):
    if n == 0:
        return
    print(n, end=' ')
    even(n-1)

N = int(input())

odd(N)
print()
even(N)