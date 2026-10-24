nums = [4, 2, 1, 7, 3, 2]
k = 3

window_sum = sum(nums[:k])
maximum = window_sum

for i in range(len(nums) - k):
    window_sum -= nums[i]
    window_sum += nums[i + k]
    if window_sum > maximum:
        maximum = window_sum
        
print(window_sum)