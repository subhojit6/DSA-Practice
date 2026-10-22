nums = [10, 20, 30, 40, 50, 60]
k = 3
k = k % len(nums)
l1 = k
l2 = len(nums) - 1

while l1 < l2:
    temp = nums[l1]
    nums[l1] = nums[l2]
    nums[l2] = temp
    l2 -= 1
    l1 += 1

print(nums)