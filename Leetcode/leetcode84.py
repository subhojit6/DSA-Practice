class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for i in range(len(heights) + 1):
            current_height = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] > current_height:
                popped_index = stack.pop()
                height = heights[popped_index]
                width = i - stack[-1] - 1 if stack else i
                area = height * width
                if max_area < area:
                    max_area = area
            if i < len(heights):
                stack.append(i)
        return max_area


input = Solution()
print(input.largestRectangleArea([2, 1, 3, 4, 2]))