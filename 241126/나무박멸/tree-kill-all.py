def remove():
    for y in range(n):
        for x in range(n):
            if time_graph[y][x] > 0:
                time_graph[y][x] -= 1

def growth():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    temp_graph = [row[:] for row in graph]

    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0:
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] > 0:
                            count += 1
                temp_graph[y][x] += count
    for y in range(n):
        for x in range(n):
            graph[y][x] = temp_graph[y][x]

def breeding():
    breeding_graph = [list(0 for _ in range(n)) for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0:
                count = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] == 0 and time_graph[ny][nx] == 0:
                            count += 1
                if count > 0:
                    spread_amount = graph[y][x] // count
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[ny][nx] == 0 and time_graph[ny][nx] == 0:
                                breeding_graph[ny][nx] += spread_amount
    for y in range(n):
        for x in range(n):
            graph[y][x] += breeding_graph[y][x]

def spraying():
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]

    max_count = -1
    max_x, max_y = -1, -1

    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0:
                count = graph[y][x]
                for d in range(4):
                    for dd in range(1, k+1):
                        nx = x + dx[d] * dd
                        ny = y + dy[d] * dd
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[ny][nx] == -1:
                                break
                            elif graph[ny][nx] == 0:
                                break
                            else:
                                count += graph[ny][nx]
                        else:
                            break
                if count > max_count:
                    max_count, max_x, max_y = count, x, y
                elif count == max_count:
                    if y < max_y or (y == max_y and x < max_x):
                        max_x, max_y = x, y

    total_killed = 0
    if max_x != -1 and max_y != -1:
        if graph[max_y][max_x] > 0:
            total_killed += graph[max_y][max_x]
        graph[max_y][max_x] = 0
        time_graph[max_y][max_x] = c + 1
        for d in range(4):
            for dd in range(1, k+1):
                nx = max_x + dx[d] * dd
                ny = max_y + dy[d] * dd
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[ny][nx] == -1:
                        break
                    time_graph[ny][nx] = c + 1
                    if graph[ny][nx] == 0:
                        break
                    else:
                        total_killed += graph[ny][nx]
                        graph[ny][nx] = 0
                else:
                    break
    return total_killed

n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time_graph = [list(0 for _ in range(n)) for _ in range(n)]
answer = 0

for year in range(m):
    remove()    # 제초제 지속 시간 감소
    growth()    # 나무 성장
    breeding()  # 나무 번식
    answer += spraying()  # 제초제 살포

print(answer)
