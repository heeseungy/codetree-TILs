dic = {1: "John", 2: "Tom", 3: "Paul", 4: "Sam"}

while True:
    num = int(input())

    if num in dic:
        print(dic[num])
    else:
        print("Vacancy")
        break