## Runtime: 64 ms, faster than 84.93% of Python online submissions for Remove Duplicates from Sorted Array.
## Memory Usage: 14.4 MB, less than 92.08% of Python online submissions for Remove Duplicates from Sorted Array.

class Solution:
    def removeDuplicates(self, nums):
        j = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
