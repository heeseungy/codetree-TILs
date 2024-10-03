n = int(input())

# 1~n년까지 윤년은 총 몇번?
# 윤년 = 4로 나누어 떨어짐
# 단, 100으로 나누어 떨어지되 400으로 나누어 떨어지지 않으면 평년임

cnt = 0

for i in range(1, n+1):
    if i % 100 == 0 and i % 400 != 0:
        continue
    elif i % 4 == 0:
        cnt += 1

print(cnt)