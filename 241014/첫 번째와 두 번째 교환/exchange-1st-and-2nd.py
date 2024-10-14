s = list(input())

first, second = s[0], s[1]

result = []
for i in range(len(s)):
    if s[i] == first:
        result.append(second)
    elif s[i] == second:
        result.append(first)
    else:
        result.append(s[i])

print(''.join(map(str, result)))