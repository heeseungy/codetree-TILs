n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

ans, cnt = 0, 0
for i in range(n):
	if i >= 1 and arr[i] * arr[i - 1] > 0:
		cnt += 1
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)