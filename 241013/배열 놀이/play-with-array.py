# n, q 입력
n, q = map(int, input().split())

# 원소들 입력
arr = list(map(int, input().split()))

# 질의 q번 입력
ques = [list(map(str, input().split())) for _ in range(q)]

for qu in ques:
    if int(qu[0]) == 1:
        # "1 a"의 경우 a번째 원소를 출력
        print(arr[int(qu[1]) - 1])
    elif int(qu[0]) == 2:
        # "2 b"의 경우 값이 b인 원소 중 가장 작은 인덱스를 출력
        found = False
        for i in range(len(arr)):
            if arr[i] == int(qu[1]):
                print(i + 1)
                found = True
                break
        if not found:
            print(0)
    else:
        # "3 s e"의 경우 s부터 e까지의 원소를 출력
        s = int(qu[1]) - 1
        e = int(qu[2])
        print(" ".join(map(str, arr[s:e])), end=' ')
        print()  # 줄바꿈을 위해 추가