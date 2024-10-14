string = input()

if len(string) % 2 == 0:
    for i in range(len(string)-1, -1, -2):
        print(string[i], end='')
else:
    for i in range(len(string)-2, -1, -2):
        print(string[i], end='')