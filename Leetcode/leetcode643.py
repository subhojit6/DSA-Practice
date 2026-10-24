nums = [1, 12, -5, -6, 50, 3]
k = 4

left = 0
window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(len(nums) - k):
    window_sum -= nums[left]
    window_sum += nums[i + k]
    if window_sum > max_sum:
        max_sum = window_sum
    left += 1

print(max_sum / k)

