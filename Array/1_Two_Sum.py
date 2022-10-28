class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


arr = [2, 7, 11, 15]
obj = Solution()
print(obj.twoSum(arr, 9))
