def func(row, col):
    for _ in range(row):
        for _ in range(col):
            print(1, end='')
        print()

n, m = map(int, input().split())

func(n, m)