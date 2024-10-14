n = int(input())
info = []
for i in range(1, n+1):
    h, w = map(int, input().split())
    info.append([h, w, i])

info.sort(key=lambda x: (-x[0], -x[1], x[2]))

for i in info:
    print(*i)