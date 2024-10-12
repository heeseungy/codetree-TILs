cube = list(map(int, input().split()))
count_list = list(0 for _ in range(7))

for c in cube:
    count_list[c] += 1

for i in range(1, 7):
    print(f"{i} - {count_list[i]}")