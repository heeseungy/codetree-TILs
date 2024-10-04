n = int(input())

num = 1

while True:
    n = n // num
    if n <= 1:
        break
    num += 1

print(num)