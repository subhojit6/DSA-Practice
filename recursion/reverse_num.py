def reverse_integer(num):
    sign = -1 if num < 0 else 1
    return reverse_number(abs(num), 0) * sign

def reverse_number(num, reversed_num):
    if num:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        return reverse_number(num // 10, reversed_num)
    else:
        return (reversed_num)
num = -1234
print(reverse_integer(num))