class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minLength = float("inf")
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minLength = min(minLength, r - l + 1)
                curSum -= nums[l]
                l += 1
                 
        return 0 if minLength == float("inf") else minLength 