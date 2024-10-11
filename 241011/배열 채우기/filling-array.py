# 정수를 입력받다가 0이 입력되면 끝나지 않았더라도 입력 중단
# 현재까지 입력받은 배열을 뒤집어서 출력

arr = list(map(int, input().split()))

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])
    else:
        result.reverse()
        break

print(*result)