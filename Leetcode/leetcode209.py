nums = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
right = 0
window_sum = 0
win_length = float('inf')

while right < len(nums):
    window_sum += nums[right]

    while window_sum >= target:
        current_length = right - left + 1
        if current_length < win_length:
            win_length = current_length
        window_sum -= nums[left]
        left += 1
    right += 1


print(win_length)
