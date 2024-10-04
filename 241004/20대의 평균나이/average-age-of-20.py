total = 0
cnt = 0
while True:
    age = int(input())
    if age // 10 == 2:
        cnt += 1
        total += age
    else:
        print(f"{total/cnt:.2f}")
        break