a, b = map(str, input().split())

max_val = max(a, b)
min_val = min(a, b)

print(ord(max_val) + ord(min_val), ord(max_val) - ord(min_val))