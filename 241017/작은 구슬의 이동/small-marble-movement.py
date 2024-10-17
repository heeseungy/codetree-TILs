# n행 n열 칸에 구슬
# 상하좌우 중 특정방향으로 1초에 1칸 움직임
# 구슬이 벽에 부딪히면 움직이는 방향 반대로 뒤집어짐 (방향전환에 1초 소요)

n, t = map(int, input().split())
r, c, d = input().split()

r, c = int(r) - 1, int(c) - 1

# 상 좌 하 우
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direct = 0
if d == 'U':
    direct = 0
elif d == 'L':
    direct = 1
elif d == 'D':
    direct = 2
else:
    direct = 3

for i in range(t):
    nx = r + dx[direct]
    ny = c + dy[direct]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        r, c = nx, ny
    else:
        direct = (direct + 2) % 4

print(c, r)