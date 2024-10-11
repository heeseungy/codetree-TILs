# 정수 10개 입력 -> 합 / 평균 출력
# 0이 입력되면 빼고 합과ㅏ 평균

arr = list(map(int, input().split()))

result = []

for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])
    else:
        break

val = sum(result)
avg = val / len(result)

print(f"{val} {avg:.1f}")