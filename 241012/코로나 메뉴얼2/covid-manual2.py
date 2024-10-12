# 감기증상 있으면 Y / 없으면 N

# Y / 37이상 > A
# N / 37이상 > B
# Y / 37미만 > C
# N / 37미만 > D

# A가 2명 이상 -> 위급상황(E)

# 출력: 진료소(A, B, C, D)로 보내지는 인원수 + E일 경우만 E 출력

arr = [list(map(str, input().split())) for _ in range(3)]
cnt = [0 for _ in range(4)]

for a in arr:
    if a[0] == 'Y' and int(a[1]) >= 37:
        cnt[0] += 1
    elif a[0] == 'N' and int(a[1]) >= 37:
        cnt[1] += 1
    elif a[0] == 'Y' and int(a[1]) < 37:
        cnt[2] += 1
    else:
        cnt[3] += 1

print(*cnt, end=' ')
if cnt[0] >= 2:
    print('E')