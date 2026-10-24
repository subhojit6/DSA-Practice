nums = [1, 2, 3, 4]

for i in range(0, len(nums) - 1):
    nums[i + 1] = nums[i] + nums[i + 1]

print(nums)