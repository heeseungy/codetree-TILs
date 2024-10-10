a, b = map(int, input().split())

for i in range(2, 9, 2):
    print(' / '.join(f"{j} * {i} = {j*i}" for j in range(b, a-1, -1)))