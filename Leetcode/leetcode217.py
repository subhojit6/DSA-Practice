nums = [1, 2, 4, 6, 7, 2, 6]

seen = set()

for num in nums:
    if num in seen:
        print(True)
        break
    else:
        seen.add(num)
else:
    print(False)