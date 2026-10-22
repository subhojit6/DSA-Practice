nums = [4, 7, 2, 4, 9, 7, 4]

seen = set()

for i, num in enumerate(nums):
    if num in seen:
        print(num)
        break
    else:
        seen.add(num)