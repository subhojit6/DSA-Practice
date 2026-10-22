nums = [4, 8, 12, 16, 20]

temp = nums[1]
nums[1] = nums[3]
nums[3] = temp
print(nums)