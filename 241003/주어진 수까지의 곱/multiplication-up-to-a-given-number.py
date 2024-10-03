a, b = map(int, input().split())

val = 1

for i in range(a, b+1):
    val *= i

print(val)