def calc(n):
    print(n, end=' ')
    if n == 1:
        print(n, end=' ')
        return
    calc(n-1)
    print(n, end=' ')
    

n = int(input())

calc(n)