s = input()

for i in range(len(s) + 1, 0, -1):
    print(s[i-1:] + s[:i-1])