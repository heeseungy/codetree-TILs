s = list(input())

same = s[1]

for i in range(1, len(s)):
    if s[i] == same:
        s[i] = s[0]

print(''.join(map(str, s)))