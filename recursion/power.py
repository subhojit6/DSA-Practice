def power(base, exp):

    if exp == 0:
        return 1

    negative = exp < 0
    exp = abs(exp)

    half = power(base, exp // 2)

    if exp % 2 == 0:
        result = half * half
    else:
        result = base * half * half

    if negative:
        return 1 / result
    else:
        return result
            
            
print(power(3, -5))