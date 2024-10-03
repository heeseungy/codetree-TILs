# 남자는 0, 여자는 1
# 성인 >= 19세

# MAN, WOMAN / BOY, GIRL 을 구분하시오

sex = int(input())
age = int(input())

if sex == 0:
    if age >= 19:
        print('MAN')
    else:
        print('BOY')
else:
    if age >= 19:
        print('WOMAN')
    else:
        print('GIRL')