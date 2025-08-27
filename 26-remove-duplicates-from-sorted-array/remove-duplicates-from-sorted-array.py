class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=1
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]!=nums[i]:
                nums[k]=nums[i]
                k+=1
        return k