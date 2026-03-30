class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ret = []
        currSum = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[i] + nums[r] + nums[l]
                if currSum > 0:
                    r -= 1
                if currSum < 0:
                    l += 1
                if currSum == 0:
                    ret.append([nums[i], nums[r], nums[l]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ret