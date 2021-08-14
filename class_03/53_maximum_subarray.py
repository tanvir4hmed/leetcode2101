class Solution(object):
    def maxSubArray(self, nums):
        maxv = nums[0]
        for i, num in enumerate(nums):
            temp = 0
            for j in range(i, len(nums)):
                temp = temp + nums[j]
                if temp >= maxv:
                    maxv = temp
                j += 1
        return maxv