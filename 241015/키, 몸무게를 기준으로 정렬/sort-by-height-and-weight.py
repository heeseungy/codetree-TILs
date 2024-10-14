n = int(input())
info = [list(map(str, input().split())) for _ in range(n)]

# 키(오름차순) > 몸무게(내림차순)
for i in range(len(info)):
    info[i][1] = int(info[i][1])
    info[i][2] = int(info[i][2])

info.sort(key=lambda x: (x[1], -x[2]))

for i in info:
    print(*i)