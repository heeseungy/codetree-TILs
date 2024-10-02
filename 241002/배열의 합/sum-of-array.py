graph = [list(map(int, input().split())) for _ in range(4)]

for i in graph:
    total = 0
    for j in i:
        total += j
    print(total)