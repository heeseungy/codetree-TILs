n = int(input())
people = [list(map(str, input().split())) for _ in range(n)]

people.sort(key=lambda x: (int(x[1]) + int(x[2]) + int(x[3])))

for p in people:
    print(*p)