def print_nums(num):

    # 1. Base case
    if num > 10:
        return

    print(num)

    print_nums(num + 1)

print_nums(1)