# (0, 0) / 북쪽 바라봄 (시작)

# N개의 명령에 따라 N번 움직임
# L명령: 좌향좌
# R명령: 우향우
# F명령: 앞으로가(1칸)

# 최종위치는?

x, y = 0, 0
dir = 1
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]   # 좌 상 우 하

command = list(input())

for i in range(len(command)):
    if command[i] == 'L':
        dir = (dir + 3) % 4
    elif command[i] == 'R':
        dir = (dir + 1) % 4    
    else:   # F
        x = x + dx[dir]
        y = y + dy[dir]
    
print(x, y)