nums = [2, 4, 6, 5, 8]

sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        sorted = False
        break

if sorted:
    print("Sorted")
else:
    print("Not sorted")