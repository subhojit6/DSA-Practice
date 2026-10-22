nums = [12, -5, 8, 20, 3, -10]

smallest_number = nums[0]

for num in nums:
    if smallest_number > num:
        smallest_number = num

print(smallest_number)
