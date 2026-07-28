class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_a = float('-inf')
        while left < right:
            diff = right - left
            if heights[left] < heights[right]:
                max_a = max(max_a, heights[left] * diff)
                left += 1
            else:
                max_a = max(max_a, heights[right] * diff)
                right -= 1
        return max_a