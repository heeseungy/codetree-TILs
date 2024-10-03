a, b = map(int, input().split())

val = 1

for i in range(1, b+1):
    if i % a == 0:
        val *= i
    
print(val)