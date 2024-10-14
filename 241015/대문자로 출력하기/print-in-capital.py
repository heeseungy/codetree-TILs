s = list(input())

for a in s:
    if ord(a) >= 65 and ord(a) <= 122:
        print(a.upper(), end='')