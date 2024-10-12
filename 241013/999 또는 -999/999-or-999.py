inputs = input()

nums = []
for num in inputs.split():
    if int(num) == 999 or int(num) == -999:
        break
    nums.append(int(num))

print(max(nums), min(nums))