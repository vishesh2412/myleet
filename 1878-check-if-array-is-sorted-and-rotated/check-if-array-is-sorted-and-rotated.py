class Solution:
    def check(self, nums: List[int]) -> bool:
        drops=0
        length=len(nums)
        for i in range(length):
            if nums[i]>nums[(i+1)%length]:
                drops+=1
                if drops>1:
                    return False
        return True