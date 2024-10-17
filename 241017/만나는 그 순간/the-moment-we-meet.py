n, m = map(int, input().split())

a_moves = []
b_moves = []

for _ in range(n):
    d, t = input().split()
    t = int(t)
    direction = -1 if d == 'L' else 1
    a_moves.extend([direction] * t)

for _ in range(m):
    d, t = input().split()
    t = int(t)
    direction = -1 if d == 'L' else 1
    b_moves.extend([direction] * t)

a_position = 0
b_position = 0

max_time = len(a_moves)

for time in range(max_time):
    a_position += a_moves[time]
    b_position += b_moves[time]
    
    if a_position == b_position:
        print(time + 1)
        break
else:
    print(-1)