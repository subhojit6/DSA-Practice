n = 7
seen = set()

def sum_of_square_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 2
        n = n // 10
    return total

while n != 1 and n not in seen:
    seen.add(n)
    n = sum_of_square_digits(n)


if n == 1:
    print(True)
else:
    print(False)

print(seen)