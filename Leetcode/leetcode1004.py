nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

left = 0
max_len = 0
z_count = 0

for right in range(len(nums)):
    if nums[right] == 0:
        z_count += 1

    while z_count > k:
        if nums[left] == 0:
            z_count -= 1
        left += 1

    curr_length = right - left + 1
    if curr_length > max_len:
        max_len = curr_length

print(max_len)

    