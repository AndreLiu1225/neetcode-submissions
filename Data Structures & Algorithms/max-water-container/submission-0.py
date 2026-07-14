class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            max_area = max(w * h, max_area)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area