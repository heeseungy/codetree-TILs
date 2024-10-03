n = int(input())

val = 1

for i in range(1, 11):
    if val >= n:
        print(val)
        break
    
    val *= i