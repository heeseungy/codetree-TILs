n, m, k = map(int, input().split())

ans = 0
students = [0 for _ in range(n + 1)]

# 벌칙 걸린 학생의 번호 배열
bad = list(int(input()) for _ in range(m))

for i in range(m):
    num = bad[i]
    students[num] += 1
    if students[num] == k:
        ans = num
        break

print(ans)