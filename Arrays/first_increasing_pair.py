nums = [9, 7, 5, 8, 3, 1, 6]

for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        print(f"{nums[i]} is smaller than {nums[i + 1]}")
        break