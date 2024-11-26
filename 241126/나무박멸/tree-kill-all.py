#제초제 유효기간 감소 함수
def remove():
    for y in range(n):
        for x in range(n):
            if time_graph[y][x] > 0:
                time_graph[y][x] -= 1

# 성장
def growth():

    # dx, dy 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(n):
            # 나무가 있을 경우, 주변 인접나무 찾기
            if graph[y][x] > 0:
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] > 0:
                            count += 1

                # 주변 인접나무만큼 성장하기
                graph[y][x] += count

# 번식
def breeding():
    breeding_graph = [list(0 for _ in range(n)) for _ in range(n)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(n):
            # 번식 가능한 칸 확인
            if graph[y][x] > 0:
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] == 0 and time_graph[ny][nx] == 0:
                            count += 1
                # 찐번식할 나무 수 임시배열 옮기기
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] == 0 and time_graph[ny][nx] == 0:
                            breeding_graph[ny][nx] += (graph[y][x] // count)
    # 찐번식
    for y in range(n):
        for x in range(n):
            graph[y][x] += breeding_graph[y][x]


# 제초제 살포
def spraying():

    # 좌상, 우상, 좌하, 우하
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]

    max_count, max_x, max_y = -1, -1, -1

    for y in range(n):
        for x in range(n):
            # 나무가 있을 경우, 해당 칸에 살포 시 죽는 나무 수 세기
            if graph[y][x] > 0:
                count = graph[y][x]
                for d in range(4):
                    for dd in range(1, k+1):
                        nx = x + (dx[d] * dd)
                        ny = y + (dy[d] * dd)
                        if 0 <= nx < n and 0 <= ny < n:
                            # 벽 있을 때, 살포중단
                            if graph[ny][nx] == -1:
                                break
                            # 나무가 없을 때, 살포중단
                            if graph[ny][nx] == 0:
                                break
                            else:
                                count += graph[ny][nx]
                # max 값 갱신하기
                if count > max_count:
                    max_count, max_x, max_y = count, x, y

    # 최대 살육위치에 제초제 살포
    if max_x != -1 and max_y != -1:
        graph[max_y][max_x] = 0
        time_graph[max_y][max_x] = c + 1
        for d in range(4):
            for dd in range(1, k+1):
                nx = max_x + (dx[d] * dd)
                ny = max_y + (dy[d] * dd)
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[ny][nx] == -1: # 벽인 경우 더이상 안뿌림
                        break
                    time_graph[ny][nx] = c + 1
                    if graph[ny][nx] == 0:  # 나무가 존재하지 않는 경우
                        break
                    else:   # 벽이 아니고 나무가 존재하는 경우
                        graph[ny][nx] = 0

    # 최대살육 나무 수 리턴
    return max_count

n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 나무, 벽 입력 그래프
time_graph = [list(0 for _ in range(n)) for _ in range(n)]  # 제초제 유효기간 그래프
answer = 0  # m년동안 죽인 전체 나무 수

for year in range(m):
    remove()    # 제초제 유효기간 감소
    growth()    # 성장
    breeding()  # 번식
    answer += spraying()  # 제초제 살포

print(answer)
