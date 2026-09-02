class Solution(object):
    def productExceptSelf(self, nums):

        answer = [1] * len(nums)

        # Product of everything to the left
        left = 1
        for i in range(len(nums)):
            answer[i] = left
            left *= nums[i]

        # Product of everything to the right
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer