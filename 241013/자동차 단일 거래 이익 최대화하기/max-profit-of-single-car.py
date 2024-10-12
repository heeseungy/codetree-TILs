n = int(input())
price = list(map(int, input().split()))

lowest = price[0]
gap = 0
for i in range(1, len(price)):
    if price[i] < lowest:
        lowest = price[i]
    else:
        if price[i] - lowest > gap:
            gap = price[i] - lowest

print(gap)