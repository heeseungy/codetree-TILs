n = int(input())
arr = list(map(int, input().split()))
print(' '.join([str(elem**2) for elem in arr]))