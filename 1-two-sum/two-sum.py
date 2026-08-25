class Solution(object):
    def twoSum(self, nums, target):
        dict1={}

        for index,value in enumerate(nums):
            find_number=target-value

            if find_number in dict1:
                return [index,dict1[find_number]]

            dict1[value]=index
