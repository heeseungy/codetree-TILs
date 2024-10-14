def check(a, b):
    if len(a) != len(b):
        return 'No'
    for i in range(len(a)):
        if a[i] != b[i]:
            return 'No'
    return 'Yes'

a = list(input())
b = list(input())

a.sort()
b.sort()

print(check(a, b))