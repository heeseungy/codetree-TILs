string = list(input())
string.reverse()
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i], end='')