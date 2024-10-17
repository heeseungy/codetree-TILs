n = int(input())

x, y = 0, 0

# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    d, m = map(str, input().split())
    if d == 'E':
        x += dx[0]
        y += dy[0]
    elif d == 'S':
        x += dx[1]
        y += dy[1]
    
    elif d == 'W':
        x += dx[2]
        y += dy[2]
    
    elif d == 'N':
        x += dx[3]
        y += dy[3]