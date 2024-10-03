patients = [list(map(str, input().split())) for _ in range(3)]

cnt = 0

for p in patients:
    if p[0] >= 'Y' and int(p[1]) >= 37:
        cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')