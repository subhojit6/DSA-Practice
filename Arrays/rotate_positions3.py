nums = [10, 20, 30, 40, 50, 60]
k = 3
k = k % len(nums)
l = k - 1

for i in range(k // 2):
    temp = nums[i]
    nums[i] = nums[l]
    nums[l] = temp
    l -= 1


print(nums)