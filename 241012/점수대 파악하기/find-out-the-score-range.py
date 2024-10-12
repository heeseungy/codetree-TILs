score = list(map(int, input().split()))
cnt = list(0 for _ in range(11))

for s in score:
    if s == 0:
        break
    val = s // 10
    cnt[val] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt[i]}")