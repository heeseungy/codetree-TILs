n = int(input())

val = 0

for i in range(1, 101):
    val += i
    if val >= n:
        print(i)
        break