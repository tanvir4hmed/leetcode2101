# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

# a = [1,2,3,4]
# result = []
# start = len(a)-1
# end = 0
# while start >=0:
#     result.append(a[start])
# print(result)

a = [1,2,3,4]
start = 0
end = len(a)-1
while start < end:
    temp = a[start]
    a[start] = a[end]
    a[end] = temp
    start += 1
    end -= 1

print(a)

