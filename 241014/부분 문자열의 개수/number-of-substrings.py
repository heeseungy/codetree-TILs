A = input()
B = input()

cnt = 0
for i in range(len(A) - 1):
    if A[i:i+2] == B:
        cnt += 1

print(cnt)