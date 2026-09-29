class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area, l, r = 0, 0, len(heights) - 1

        while l < r:
            cur_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, cur_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

        # O(n) time; O(1) space
