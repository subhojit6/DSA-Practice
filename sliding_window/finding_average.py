nums = [2, 1, 5, 1, 3, 2]
k = 3

avg_window = sum(nums[:k])
max_sum = avg_window

for i in range(len(nums) - k):
    avg_window -= nums[i]
    avg_window += nums[i + k]
    if max_sum < avg_window:
        max_sum = avg_window

max_avg = max_sum / k

print(max_avg)
