# n, q 입력
n, q = map(int, input().split())

# 원소들 입력
arr = list(map(int, input().split()))

# 질의 q번 입력
ques = [list(map(str, input().split())) for _ in range(q)]

for qu in ques:
    if int(qu[0]) == 1:
        print(arr[int(qu[1]) - 1])
    elif int(qu[0]) == 2:
        for i in range(len(arr)):
            if arr[i] == int(qu[1]):
                print(i+1)
        else:
            print(0)
    else:
        for i in range(int(qu[1]), int(qu[2]) + 1):
            print(arr[i-1], end=' ')

# 1 a > a번째 원소를 출력
# 2 b > 원소 n개 중 값이 b인 원소가 몇번째 원소인지 출력
# 3 s e > s ~ e번째 원소값을 공백으로 구분하여 차례대로 출력

# q개의 줄에 걸쳐 질의가 주어짐