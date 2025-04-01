class Solution(object):
    def twoSum(self, nums, target):
        list1=[]
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                if(a+nums[j]==target):
                    list1.extend([i,j])
                    break
        return list1