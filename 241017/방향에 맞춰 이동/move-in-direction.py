# (0, 0)에서 출발

# N번 이동

# N번에 걸쳐 움직이는 방향, 이동거리가 주어짐

# 최종위치는?

x, y = 0, 0

n = int(input())
for _ in range(n):
    d, m = input().split()
    m = int(m)

    if d == 'N':
        y += m
    elif d == 'E':
        x += m
    elif d == 'S':
        y -= m
    else:
        x -= m

print(x, y)