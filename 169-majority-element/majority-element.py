class Solution(object):
    def majorityElement(self, nums):
        dict1={}
        a=set(nums)
        for i in a:
            dict1[i]=nums.count(i)
        maxv=0
        maxi=0
        for i in dict1:
            if dict1[i]>maxv:
                maxv=dict1[i]
                maxi=i
        return maxi
        
         