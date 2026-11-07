nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

stack = []
next_greater = {}

for num in nums2:
    while stack and num > stack[-1]:
        next_greater[stack[-1]] = num
        stack.pop()
    stack.append(num)

for num in stack:
    next_greater[num] = -1

for i in range(len(nums1)):
    nums1[i] = next_greater[nums1[i]]

print(nums1)
    
    
