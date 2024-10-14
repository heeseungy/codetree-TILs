n, k, T = map(str, input().split())

words = []
for _ in range(int(n)):
    words.append(input())

words.sort()

cnt = 0
for w in words:
    if T in w:
        cnt += 1
    
    if cnt == int(k):
        print(w)
        break