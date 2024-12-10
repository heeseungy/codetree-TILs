n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)] # 나무 정보

medicine = [[0] * n for _ in range(n)]  # 특수 영양제 정보
medicine[n-1][0] = 1
medicine[n-1][1] = 1
medicine[n-2][0] = 1
medicine[n-2][1] = 1

moving_rule = [list(map(int, input().split())) for _ in range(m)]   # 이동규칙 정보

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def moving(year, medicine):
    d, p = moving_rule[year][0] - 1, moving_rule[year][1]   # d: 이동방향 / p: 이동칸

    # d방향으로 p만큼 이동
    tmp_medicine = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            # 영양제가 있다면 이동한다
            if medicine[y][x] == 1:
                # nx, ny를 구하고 격자를 벗어나는 경우 반대편으로 돌아오는 예외를 처리한다
                nx = x + (dx[d] * p)
                ny = y + (dy[d] * p)

                if nx < 0:
                    nx = n - abs(nx)
                elif nx >= n:
                    nx = nx % n

                if ny < 0:
                    ny = n - abs(ny)
                elif ny >= n:
                    ny = ny % n

                tmp_medicine[ny][nx] = 1

    return tmp_medicine

def injection(graph, medicine):

    # graph랑 medicine 비교하면서 영양제 투입 및 소멸
    for y in range(n):
        for x in range(n):
            if medicine[y][x] == 1:
                graph[y][x] += 1    # 특수영양제 있는 땅 = 1만큼 성장

    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]

    # 대각에 있는 만큼 추가 성장
    for y in range(n):
        for x in range(n):
            if medicine[y][x] == 1:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[ny][nx] > 0:
                            cnt += 1
                graph[y][x] += cnt

    return graph

def buying(graph, medicine):
    # 특수영양제 구입
    # 해당연도에 맞은 곳은 제외
    tmp_medicine = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if graph[y][x] >= 2 and medicine[y][x] != 1:
                graph[y][x] -= 2
                tmp_medicine[y][x] = 1

    return tmp_medicine

for year in range(m):
    medicine = moving(year, medicine)    # 특수영양제 이동
    graph = injection(graph, medicine)   # 특수영양제 투입 및 소멸
    medicine = buying(graph, medicine)    # 특수영양제 구입

# m년 후의 남아있는 리브로수의 총 높이의 합은?
answer = 0
for g in graph:
    answer += sum(g)

print(answer)
