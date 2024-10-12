lebros = list('LEBROS')

s = input()

for i in range(len(lebros)):
    if lebros[i] == s:
        print(i)
        break
else:
    print('None')