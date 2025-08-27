class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k, n):
            nums[i] = 0
        