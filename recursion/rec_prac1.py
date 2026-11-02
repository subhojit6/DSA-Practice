def add_nums(num):
    if num == 1:
        return 1
    return  num + add_nums(num - 1)
    
print(add_nums(5))