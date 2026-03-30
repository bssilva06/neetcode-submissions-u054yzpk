class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        curSum = 0

        while l < r:
            curSum = numbers[l] + numbers[r]
            while l < r and curSum > target:
                r -= 1
                curSum = numbers[l] + numbers[r]
            while l < r and curSum < target:
                l += 1
                curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l + 1, r + 1]
        return []