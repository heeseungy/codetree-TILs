def print_sequence(a, b):
    current = a
    while current <= b:
        print(current, end=' ')
        if current % 2 == 0:
            current += 3
        else:
            current *= 2

a, b = 2, 13
print_sequence(a, b)