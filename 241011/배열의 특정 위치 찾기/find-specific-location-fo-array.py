arr = list(map(int, input().split()))

val, avg = 0, 0

for i in range(len(arr)):
    if i % 2 == 1:
        val += arr[i]
    if i % 3 == 2:
        avg += arr[i]

print(f"{val} {avg/3:.1f}")