cnt, val = 0, 0
for _ in range(10):
    n = int(input())

    if 0 <= n and n <= 200:
        cnt += 1
        val += n

print(f"{val} {val/cnt:.1f}")