nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
maximum = window_sum

for i in range(len(nums) - k):
    window_sum -= nums[i]
    window_sum += nums[i + k]
    if maximum < window_sum:
        maximum = window_sum

print(maximum)