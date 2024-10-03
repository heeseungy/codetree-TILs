n = int(input())

num = 1
while num <= n:
    # 3의 배수인가?
    if num % 3 == 0:
        print(0, end=' ')
    # 숫자에 3, 6, 9중 하나가 들어가는가? = 1의 자리와 10의 자리에 3, 6, 9가 들어가는가?
    elif (num % 10) in (3, 6, 9):
        print(0, end=' ')
    elif (num / 10) in (3, 6, 9):
        print(0, end=' ')
    else:
        print(num, end=' ')
    num += 1