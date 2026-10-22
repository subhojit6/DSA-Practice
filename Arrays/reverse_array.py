nums = [10, 20, 30, 40, 50]

last_index = len(nums) - 1

for i in range(len(nums) // 2):
    temp = nums[i]
    nums[i] = nums[last_index]
    nums[last_index] = temp
    last_index -= 1

print(nums)