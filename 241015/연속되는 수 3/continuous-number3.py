n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

current_cnt = 1
max_cnt = 1

sign = ''
if arr[0] > 0:
    sign = 'plus'
else:
    sigin = 'minus'

for i in range(1, n):
    if sign == 'plus' and arr[i] > 0:
        current_cnt += 1
        max_cnt = max(max_cnt, current_cnt)
    elif sign == 'minus' and arr[i] < 0:
        current_cnt += 1
        max_cnt = max(max_cnt, current_cnt)
    elif sign == 'plus' and arr[i] < 0:
        current_cnt = 1
        sign = 'minus'
    else:
        current_cnt = 1
        sign = 'plus'

print(max_cnt)