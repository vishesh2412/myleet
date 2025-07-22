class Solution(object):
    def maximumUniqueSubarray(self, nums):
        left=0
        total=0
        usum=0
        unique=set()
        for i in range(len(nums)):
            while nums[i] in unique:
                unique.remove(nums[left])
                usum-=nums[left]
                left+=1
            unique.add(nums[i])
            usum+=nums[i]
            total=max(total,usum)
        return total