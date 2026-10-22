nums = [5, 12, 7, 20, 15]

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print(f"{nums[i]} is greater than {nums[i + 1]}")