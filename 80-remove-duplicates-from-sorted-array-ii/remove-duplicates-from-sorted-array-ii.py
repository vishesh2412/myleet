class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while(i<len(nums)-2):
            if(nums[i]==nums[i+2]):
                nums.remove(nums[i+2])
            else:
                i+=1
                continue
        return len(nums)