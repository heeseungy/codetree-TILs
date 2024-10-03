def print_sequence(a, b):
    current = a
    while current <= b:
        print(current, end=' ')
        if current % 2 == 0:
            current += 3
        else:
            current *= 2

a, b = map(int, input().split())
print_sequence(a, b)