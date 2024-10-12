arr = list(map(int, input().split()))
count_list = [0 for _ in range(10)]

for a in arr:
    if a == 0:
        break
    
    val = a // 10
    count_list[val] += 1

for i in range(1, 10):
    print(f"{i} - {count_list[i]}")