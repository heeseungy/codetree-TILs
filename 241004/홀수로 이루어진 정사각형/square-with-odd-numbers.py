n = int(input())

for i in range(1, (n*2)+1, 2):
    for j in range(1, (n*2)+1, 2):
        print(i+j+9, end=' ')
    print()