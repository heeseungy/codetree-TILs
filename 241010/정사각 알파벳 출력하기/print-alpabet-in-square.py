n = int(input())

alpha = 65

for i in range(n):
    for j in range(n):
        print(chr(alpha), end='')
        alpha += 1
    print()