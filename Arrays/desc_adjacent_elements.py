nums = [9, 7, 5, 8, 3, 1, 6]

pairs = 0

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        pairs += 1 

print(pairs)