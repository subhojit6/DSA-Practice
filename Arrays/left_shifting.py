nums = [10, 20, 30, 40, 50]

temp = nums[0]

for i in range(len(nums) - 1):
    nums[i] = nums[i + 1]

nums[len(nums) - 1] = temp
print(nums)