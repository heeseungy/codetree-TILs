string = input()

ee, eb = 0, 0

for i in range(0, len(string) - 1, 1):
    if string[i:i+2] == 'ee':
        ee += 1
    if string[i:i+2] == 'eb':
        eb += 1

print(f"{ee} {eb}")