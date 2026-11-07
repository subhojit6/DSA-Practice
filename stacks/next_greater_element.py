nums = [2, 1, 5, 3, 4]
result = [-1] * len(nums)
stack = []

for i in range(len(nums)):
    
    while stack and nums[stack[-1]] < nums[i]:
        prev_index = stack.pop()
        result[prev_index] = nums[i]
    
    stack.append(i)

print(result)
