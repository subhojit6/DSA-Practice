def count_num(num):
    
    if num:
        return 1 + count_num(abs(num) // 10)
    else:
        return 0

print(count_num(12345))