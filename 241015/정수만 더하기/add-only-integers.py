A = input()

score = 0
for a in A:
    if a.isdigit():
        score += int(a)

print(score)