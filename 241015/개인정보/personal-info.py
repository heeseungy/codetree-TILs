info = [list(map(str, input().split())) for _ in range(5)]

# 이름, 키, 몸무게 순 입력

print('name')
info.sort(key=lambda x: x[0])
for i in info:
    print(*i)

print()

print('height')
info.sort(key=lambda x: int(x[1]), reverse=True)
for i in info:
    print(*i)