# 2일마다 교실청소
# 3일마다 복도청소
# 12일마다 화장실 청소

# 만약 날짜가 겹칠 경우, 주기가 더 긴것 (화장실 > 복도 > 교실) 진행

# n일간 진행했을 때, 각 장소의 청소횟수는?
# 단, 0일차에는 청소 진행 x

n = int(input())

cnt2, cnt3, cnt12 = 0, 0, 0

for i in range(1, n+1):
    if i % 12 == 0:
        cnt12 += 1
    elif i % 3 == 0:
        cnt3 += 1
    elif i % 2 == 0:
        cnt2 += 1

print(cnt2, cnt3, cnt12)