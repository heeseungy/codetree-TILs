a, b = map(int, input().split())

for i in range(a, b):
    if 1920 % i == 0 or 2880 % i == 0:
        print(1)
        break
else:
    print(0)