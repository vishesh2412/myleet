class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0
        for i in range(len(nums)):
            if i>reach:
                return False
            reach=max(reach,i+nums[i])
        return True