a, b, c = map(int, input().split())

flag = 0

for i in range(a, b+1):
    if i % c == 0:
        flag = 1

if flag == 1:
    print('YES')
else:
    print('NO')