n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 각 칸의 상하좌우를 검사
# if 1이 적혀있는 칸이 3개 이상인 경우 cnt += 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for direct in range(4):
            nx = i + dx[direct]
            ny = j + dy[direct]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if graph[nx][ny] == 1:
                    cnt += 1
        
        if cnt >= 3:
            ans += 1

print(ans)