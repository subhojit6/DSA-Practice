class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for i in range(len(nums)):
            self.prefix.append(self.prefix[-1] + nums[i])

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]     


obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 5)

print(param_1)