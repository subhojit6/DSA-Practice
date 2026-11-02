nums = [1,2,1]

length = len(nums)

for i in range(length):
    nums.append(nums[i])

print(nums)