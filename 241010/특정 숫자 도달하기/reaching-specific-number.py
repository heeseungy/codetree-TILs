arr = list(map(int, input().split()))

val = 0
cnt = 0

for a in arr:
    if a >= 250:
        break
    val += a
    cnt += 1

avg = val / cnt

print(f'{val} {avg:.1f}')