n = int(input())
people = list(map(int, input().split()))

# n개의 집에 모임
# 이동거리의 합이 최소가 되도록

street = 1e9

for i in range(n):
    total = 0
    for j in range(n):
        if i == j:
            continue   
        total += abs(i - j) * people[j]
    
    street = min(street, total)

print(street)