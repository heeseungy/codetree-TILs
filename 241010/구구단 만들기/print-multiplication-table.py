a, b = map(int, input().split())

for i in range(1, 10):
    print(' / '.join(f"{j} * {i} = {i*j}" for j in range(b, a-1, -1) if j % 2 == 0))