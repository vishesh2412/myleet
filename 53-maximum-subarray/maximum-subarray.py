class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        current=nums[0]
        n=len(nums)
        for i in range(1,n):
            current=max(nums[i],current+nums[i])
            max_sum=max(max_sum,current)
        return max_sum