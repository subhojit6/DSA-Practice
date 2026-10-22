nums = [10, 20, 30, 40, 50]

temp0 = nums[0]
temp1 = nums[1]

for i in range(len(nums) - 2):
    nums[i] = nums[i + 2]

nums[len(nums) - 1] = temp1
nums[len(nums) - 2] = temp0

print(nums)