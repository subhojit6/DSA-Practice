nums = [3, 8, 5, 12, 7, 20]

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] = 0


print(nums)