n = int(input())

arr = [input() for _ in range(n)]
string = input()

cnt = 0
length = 0
for a in arr:
    if a[0] == string:
        cnt += 1
        length += len(a)

avg = length/cnt
print(f"{cnt} {avg:.2f}")