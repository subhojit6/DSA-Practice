nums = [1, 2, 1, 1, 1, 3]
target = 5

left = 0
right = 0
window_sum = 0
min_length = float("inf")

while right < len(nums):
    window_sum += nums[right]

    while window_sum >= target:
        current_length = right - left + 1
        if min_length > current_length:
            min_length = current_length
        window_sum -= nums[left]
        left += 1

    right += 1

print(min_length)