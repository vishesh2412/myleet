class Solution(object):
    def canJump(self, nums):
        canreach=nums[0]
        for i in range(len(nums)):
            if i>canreach:
                return False
            canreach=max(canreach,i+nums[i])
        return True