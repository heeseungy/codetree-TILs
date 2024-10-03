n = int(input())

# 31 = 1, 3, 5, 7, 8, 10, 12
# 30 = 4, 6, 9, 11
# 28 = 2

if n in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif n in(4, 6, 9, 11):
    print(30)
else:
    print(28)