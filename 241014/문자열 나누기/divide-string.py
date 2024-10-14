n = int(input())
arr = list(map(str, input().split()))
string = ''
for a in arr:
    string += a

print(string[0], end='')
for i in range(1, len(string)):
    if i % 5 == 0:
        print()
    print(string[i], end='')