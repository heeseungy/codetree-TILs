n = int(input())
students = []
for i in range(1, n+1):
    h, w = map(int, input().split())
    students.append([h, w, i])

# 키, 몸무게 순 입력 (번호는 자동입력)
# 키(오름차순) > 몸무게(내림차순)

students.sort(key=lambda x: (x[0], -x[1]))

for s in students:
    print(*s)