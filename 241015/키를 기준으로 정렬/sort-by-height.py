n = int(input())
info = [list(map(str, input().split()) )for _ in range(n)]

info.sort(key=lambda x: x[1])

for i in info:
    print(*i)