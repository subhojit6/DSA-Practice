nums = [2, 5, 2, 8, 2, 9, 5]
target = 2
count = 0

for num in nums:
    if num == target:
        count += 1

print(count)