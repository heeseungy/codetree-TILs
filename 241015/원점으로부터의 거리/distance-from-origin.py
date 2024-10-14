n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(graph)):
    man = abs(0 - graph[i][0]) + abs(0 - graph[i][1])
    graph[i].append(man)
    graph[i].append(i+1)

graph.sort(key=lambda x: x[2])

for g in graph:
    print(g[3])