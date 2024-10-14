string = list(input())
n = int(input())

string.reverse()

if n > len(string):
    for s in string:
        print(s, end='')
else:
    for i in range(n):
        print(string[i], end='')