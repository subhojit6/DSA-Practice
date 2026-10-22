nums1 = [1, 2, 2, 1]
nums2 = [3, 2, 2]

seen = set()
result = set()

for num in nums1:
    if num not in seen:
        seen.add(num)

for num in nums2:
    if num in seen:
        result.add(num)

print(list(result))

        
        
        