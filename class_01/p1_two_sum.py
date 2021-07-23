class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = nums
        target = target
        start = 0
        end = len(a) - 1
        templist = [0, 0]
        temp = 0
        while start <= end:
            if a[start] < target:
                templist[0] = start
                temp = target - a[templist[0]]
                templist[1] = start + 1
                while templist[1] <= end:
                    if a[templist[1]] == temp:
                        temp = 0
                        break
                    templist[1] += 1
            if temp != 0:
                start += 1
            else:
                break
        if start < end and a[templist[0]] + a[templist[1]] == target:
            return templist
        else:
            return 0


if __name__ == '__main__':
    a = [2, 7, 11, 15]
    target = 8
    result = Solution.twoSum(self=Solution, nums=a, target=target)
    if result != 0:
        print(result)
    else:
        print("Not Found")
