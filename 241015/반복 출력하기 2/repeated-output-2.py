def calc(n):
    if n == 0: return
    calc(n - 1)
    print('HelloWorld')

N = int(input())

calc(N)