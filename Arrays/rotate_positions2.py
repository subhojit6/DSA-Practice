nums = [10, 20, 30, 40, 50, 60]
k = 8

k = k % len(nums)

move = []

for i in range(k):
    move.append(nums[i])

for i in range(len(nums) - k):
    nums[i] = nums[i + k]

for i in range(k):
    nums[i + k] = move[i]
 
print(nums)

