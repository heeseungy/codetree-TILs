n = int(input())

for _ in range(n):
    a = int(input())
    if a % 3 == 0 and a % 2 == 1:
        print(a)
    else:
        continue