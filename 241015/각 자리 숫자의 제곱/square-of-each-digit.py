def sum_of_squares(n):
    if n == 0:
        return 0
    else:
        last_digit = n % 10
        remaining_number = n // 10
        return last_digit**2 + sum_of_squares(remaining_number)

N = int(input())
print(sum_of_squares(N))