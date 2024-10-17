n, t = map(int, input().split())
r, c, d = input().split()
# x가 행, y가 열
x, y = int(r), int(c)

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if d == 'U':
    direct = 0
elif d == 'R':
    direct = 1
elif d == 'D':
    direct = 2
elif d == 'L':
    direct = 3

for _ in range(t):
    nx = x + dx[direct]
    ny = y + dy[direct]
    
    if not (1 <= nx <= n) or not (1 <= ny <= n):
        direct = (direct + 2) % 4
    else:
        x, y = nx, ny

print(x, y)