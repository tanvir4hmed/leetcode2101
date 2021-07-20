# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """


### Search Time Complexity O(n) MC O(1)
a = [1, 8, 13, 5, 4]
target = 5
start = 0
end = len(a)
while start < end:
    if a[start] == target:
        print("Found in index ", start)
    start += 1

# ## Reversing the list with time complexity O(n) and memory complexity O(n)
# a = [1, 2, 3, 4]
# result = []
# start = len(a) - 1
# end = 0
# while start >= 0:
#     result.append(a[start])
#     start -= 1
#
# print(result)


# ### Reversing the list with time complexity O(n) and memory complexity O(1)
# a = [1, 2, 3, 4]
# start = 0
# end = len(a) - 1
# while start < end:
#     temp = a[start]
#     a[start] = a[end]
#     a[end] = temp
#     start += 1
#     end -= 1
#
# print(a)
