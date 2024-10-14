s = input()

for a in s:
    if a.isalpha():
        print(a.lower(), end='')
    elif a.isdigit():
        print(a, end='')