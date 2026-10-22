nums = [10, 20, 30, 40, 50, 60]
k = 2
k = k % len(nums)
l = k - 1

l1 = k
l2 = len(nums) - 1

for i in range(k // 2):
    temp = nums[i]
    nums[i] = nums[l]
    nums[l] = temp
    l -= 1


while l1 < l2:
    temp = nums[l1]
    nums[l1] = nums[l2]
    nums[l2] = temp
    l2 -= 1
    l1 += 1

last_index = len(nums) - 1
for i in range(len(nums) // 2):
    temp = nums[i]
    nums[i] = nums[last_index]
    nums[last_index] = temp
    last_index -= 1

print(nums)