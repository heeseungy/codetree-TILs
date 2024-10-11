arr = list(map(int, input().split()))

even, odd = 0, 0

for i in range(len(arr)):
    if i % 2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

print(max(even, odd) - min(even, odd))