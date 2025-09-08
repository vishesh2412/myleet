class Solution(object):
    def searchInsert(self, nums, target):
        j=0
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
        for i in range(len(nums)):
            if(target>nums[i]):
                j=j+1
        return j