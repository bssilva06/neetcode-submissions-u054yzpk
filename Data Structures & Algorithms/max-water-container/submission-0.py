class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        maxWater = 0
        curArea = 0
        while L <= R:
            if heights[L] <= heights[R]:
                curArea = min(heights[R], heights[L]) * (R - L)
                if maxWater < curArea:
                    maxWater = curArea
                L += 1
            if heights[R] <= heights[L]:
                curArea = min(heights[R], heights[L]) * (R - L)
                if maxWater < curArea:
                    maxWater = curArea
                R -= 1
        
        return maxWater
