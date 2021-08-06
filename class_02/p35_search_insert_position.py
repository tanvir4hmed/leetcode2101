class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)
        while start < end and nums[start] <= target:
            if nums[start] == target:
                return start
            start += 1
        return start