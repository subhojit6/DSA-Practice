nums = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(len(nums) - k):
    window_sum -= nums[i]
    window_sum += nums[i + k]
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)