class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        for i in range(n):
            left = i
            right = i + 1

            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < n and heights[right] >= heights[i]:
                right += 1

            right -= 1
            left += 1
            width = right - left + 1

            max_area = max(width * heights[i], max_area)

        return max_area