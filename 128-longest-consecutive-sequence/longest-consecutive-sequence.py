class Solution(object):
    def longestConsecutive(self, nums):
        nums=sorted(list(set(nums)))
        if not nums:
            return 0
        length=1
        final=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                length+=1
            else:
                final=max(length,final)
                length=1
        return max(final,length)