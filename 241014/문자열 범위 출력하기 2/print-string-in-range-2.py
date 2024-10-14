string = input()
n = int(input())

length = len(string)
for i in range(length-1, length-n-1, -1):
    print(string[i], end='')