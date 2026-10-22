nums = [10, 20, 15, 25, 18, 30]

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print(f"Index {i}: {nums[i]} is greater than {nums[i + 1]}")