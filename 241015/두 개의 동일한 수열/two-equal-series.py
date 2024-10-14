n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if set(A) == set(B):
    print('Yes')
else:
    print('No')