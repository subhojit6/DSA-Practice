nums = [0,1,0,3,12]

start = 0

for num in nums:
    if num != 0:
        nums[start] = num
        start += 1

zeros = len(nums) - start

for i in range(zeros):
    nums[start] = 0
    start += 1

print(nums)
