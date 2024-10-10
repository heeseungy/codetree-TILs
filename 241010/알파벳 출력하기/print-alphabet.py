n = int(input())

alpha = 65

for i in range(1, n+1):
    for j in range(i):
        print(chr(alpha), end='')
        alpha += 1
        if alpha == 91:
            alpha = 65
    print()