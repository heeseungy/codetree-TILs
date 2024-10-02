h, w = map(int, input().split())

bmi = w/(h/100)**2

if bmi >= 25:
    print(f"{int(bmi)}\nObesity")
else:
    print(int(bmi))