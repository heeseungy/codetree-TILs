string, alpha = map(str, input().split())

if alpha in string:
    print(string.index(alpha))
else:
    print('No')