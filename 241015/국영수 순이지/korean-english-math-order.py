n = int(input())
students = [list(map(str, input().split())) for _ in range(n)]

students.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for s in students:
    print(*s)