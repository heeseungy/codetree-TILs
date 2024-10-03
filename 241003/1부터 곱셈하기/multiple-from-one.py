n = int(input())

val = 1

for i in range(1, 11):
    val *= i
    if val >= n:
        print(i)
        break