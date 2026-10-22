nums = [-4,-1,0,3,10]

r = len(nums) - 1
l = 0
pos = len(nums) - 1
ret = [0] * len(nums)

for i in range(len(nums)):
    if nums[l] ** 2 < nums[r] ** 2:
        ret[pos] = nums[r] ** 2
        r -= 1
        pos -= 1
    else:
        ret[pos] = nums[l] ** 2
        pos -= 1
        l += 1

print(ret)