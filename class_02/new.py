# Time Limit Exceeded
# Details
# Last executed input
# [-32,-54,-36,62,20,76,-1,-86,-13,38,-58,-77,17,38,-17,43,32,-88,-19,-70,95,0,-64,75,15,-87,-26,69,-95,-65,-18,-28,-43,22,-88,54,-25,-13,67,61,-74,-91,60,42,24,-80,-15,-44,-91,42,-38,-96,-58,-3,55,33,-13,-71,2,-9,-60,60,39,-26,-41,50,-72,33,-62,94,-28,-37,79,-68,81,3,-71,-57,35,-63,61,96,-83,-97,-29,48,35,57,76,-86,-52,92,50,86,-34,85,14,-30,18,51,-36,66,90,-79,75,48,0,-96,67,-64,-83,28,-91,-90,30,-44,57,-58,-87,10,-68,-63,-21,81,-76,45,66,14,-85,-39,-58,-44,-95,-68,-47,79,56,52,59,23,64,75,-49,50,61,57,-94,-5,98,95,81,-70,-68,-40,87,-68,-95,30,45,96,90,86,-71,94,94,-19,50,27,-90,9,-50,51,-39,-23,-22,-78,-66,-17,-7,-68,-22,-26,-62,-13,34,-75,18,38,54,-36,11,22,-73,39,-7,98,96,-56,25,83,52,75,34,-86,-48,-88,-88,-14,-29,5,-6,26,78,9,-87,12,10,30,-72,-58,70,15,63,97,-68,-67,95,-72,-24,20,-89,-94,-28,21,-81,1,32,-93,63,80,11,-43,6,-33,42,18,78,-47,-75,82,-6,95,-25,-66,69,6,-57,41,10,19,-62,21,1,10,-81,19,-89,28,2,73,8,-86,-93,-86,-20,49,8,-65,78,32,94,-51,27,-31,-41,-27,51,1,-86,-39,96,-48,
# View All

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