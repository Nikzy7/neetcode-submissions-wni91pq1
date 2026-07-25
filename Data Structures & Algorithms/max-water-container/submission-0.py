class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_area = 0

        while left < right:
            minimum_wall = min(heights[left], heights[right])
            current_area = (right - left) * minimum_wall

            max_area = max(current_area, max_area)

            if minimum_wall == heights[left]:
                left += 1
            else:
                right -= 1

        return max_area
