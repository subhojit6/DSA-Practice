nums = [2, 7, 11, 15]
target = 9

ret = {}

for i in range(len(nums)):
    if target - nums[i] in ret:
        print([ret[target - nums[i]], i])
    else:
        ret[nums[i]] = i
        