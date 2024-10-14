n = int(input())

words = []
for _ in range(n):
    s = input()
    words.append(s)

words.sort()

for w in words:
    print(w)