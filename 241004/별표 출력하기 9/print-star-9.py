n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end=' ')
    
    for j in range((i*2)-1):
        print('*', end=' ')
    print()


# 3

# 0 2
# 1 1
# 2 0