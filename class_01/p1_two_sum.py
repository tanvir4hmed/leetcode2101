# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

a = [2, 7, 11, 15]
target = 9
start = 0
end = len(a) - 1
templ_1 = 0
templ_2 = 0
temp = 0
while start <= end:
    if a[start] < target:
        templ_1 = start
        temp = target - a[templ_1]
        templ_2 = templ_1 + 1
        while templ_2 <= end:
            if a[templ_2] == temp:
                temp = 0
                break
            templ_2 += 1
    if temp != 0:
        start += 1
    else:
        break
if start < end and a[templ_1] + a[templ_2] == target:
    print(str(templ_1) + " and " + str(templ_2))
else:
    print("Not found")
