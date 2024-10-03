n = int(input())

cnt, val = 0, 0

for _ in range(n):
    a = int(input())
    val += a
    cnt += 1

print(f"{val} {val/cnt:.1f}")