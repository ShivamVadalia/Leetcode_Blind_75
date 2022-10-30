class Solution(object):
    def containsDuplicate(self, nums):
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False

nums = [1,2,3,1]
obj = Solution()
print(obj.containsDuplicate(nums))
