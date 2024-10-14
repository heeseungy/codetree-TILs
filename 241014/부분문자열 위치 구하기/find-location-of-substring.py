input_string = input()
goal_string = input()

if goal_string in input_string:
    print(input_string.index(goal_string))
else:
    print(-1)