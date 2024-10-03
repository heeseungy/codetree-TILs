a_kor, a_math = map(int, input().split())
b_kor, b_math = map(int, input().split())

print(((a_kor > b_kor) & (a_math > b_math)) * 1)