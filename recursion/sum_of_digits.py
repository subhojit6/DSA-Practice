def sum_of_digits(num):

    #Base case
    if num:
        return num % 10 + sum_of_digits(num // 10)
    else:
        return 0

print(sum_of_digits(1234))