n = int(input())
students = [list(map(str, input().split())) for _ in range(n)]

students.sort(key=lambda x: (int(x[1]), int(x[2]), int(x[3])), reverse=True)

for s in students:
    print(*s)