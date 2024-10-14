s = input()

print(s)
for i in range(1, len(s) + 1):
    print(s[:-i] + s[i])

# 12345
# 51234
# 45123
# 34512