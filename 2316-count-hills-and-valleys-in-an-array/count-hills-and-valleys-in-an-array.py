class Solution(object):
    def countHillValley(self, nums):
        filtered=[nums[0]]+[nums[i] for i in range(1,len(nums)) if nums[i]!=nums[i-1]]
        return sum(filtered[i-1]<filtered[i]>filtered[i+1] or filtered[i-1]>filtered[i]<filtered[i+1] for i in range(1,len(filtered)-1))