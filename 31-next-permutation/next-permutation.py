class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        if n<2:
            return nums
        
        l=n-2

        while(l>=0 and nums[l]>=nums[l+1]):
            l-=1
        
        if l>=0:
            r=n-1
            while nums[r]<=nums[l]:
                r-=1
            nums[l],nums[r]=nums[r],nums[l]

        nums[l+1:]=reversed(nums[l+1:])