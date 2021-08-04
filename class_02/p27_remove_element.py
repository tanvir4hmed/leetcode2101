## Runtime: 24 ms, faster than 42.31% of Python online submissions for Remove Element.
## Memory Usage: 13.6 MB, less than 11.34% of Python online submissions for Remove Element.

class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j