flag = 0
for _ in range(5):
    a = int(input())
    if a % 3 != 0:
        flag = 1
if flag == 0:
    print(1)
else:
    print(0)