nums = [12, 5, 8, 20, 3]

largest_number = nums[0]

for num in nums:
    if largest_number < num:
        largest_number = num

print(largest_number)