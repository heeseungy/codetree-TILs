s, q = map(str, input().split())
q = int(q)

result = list(s)
for _ in range(q):
    n, a, b = map(str, input().split())
    # result = list(s)

    # 1 a b => a번재 b번재 문자 교환 후 출력
    if n == '1':
        a, b = int(a) - 1, int(b) - 1
        tmp = result[a]
        result[a] = result[b]
        result[b] = tmp

    # 2 a b => 문자 a를 전부 문자 b로 교환 후 출력
    elif n == '2':
        for i in range(len(s)):
            if result[i] == a:
                result[i] = b
    
    print(''.join(map(str, result)))