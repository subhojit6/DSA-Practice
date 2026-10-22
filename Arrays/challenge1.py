nums = [4, 7, 4, 9, 2, 9, 9, 3]
target = 9

largest_number = nums[0]
repeated = 0
isTrue = False

for num in nums:
    if num > largest_number:
        largest_number = num

    if num == target:
        repeated += 1

    if num == target:
        isTrue = True

else:
    print(isTrue)

print(largest_number)
print(repeated)

# for num in nums:
#     if num == target:
#         print(True)
#         break
# else:
#     print(False)



