def func(side):
    num = 1

    for _ in range(side):
        for _ in range(side):
            print(num, end=' ')
            num += 1
            if num == 10:
                num = 1
        print()

N = int(input())

func(N)