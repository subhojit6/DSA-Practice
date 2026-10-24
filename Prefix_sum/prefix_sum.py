nums = [2, 4, 1, 3]
prefix = []

total = 0

for num in nums:
    total += num
    prefix.append(total)

print(prefix)