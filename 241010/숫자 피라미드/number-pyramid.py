n = int(input())

for i in range(1, n+1):
    print(' '.join(f"{i}" for _ in range(i)))