class Solution(object):
    def thirdMax(self, nums):
        nums=sorted(set(nums))
        if len(nums)>2:
            return nums[-3]
        return nums[-1]