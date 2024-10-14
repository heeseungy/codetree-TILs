s = input()

for a in s:
    if ord(a) < 98:
        print(a.lower(), end='')
    else:
        print(a.upper(), end='')