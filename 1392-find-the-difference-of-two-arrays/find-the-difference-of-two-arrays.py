class Solution(object):
    def findDifference(self, nums1, nums2):
        answer=[[],[]]
        for i in list(set(nums1)):
            if i not in nums2:
                answer[0].append(i)
        for i in list(set(nums2)):
            if i not in nums1:
                answer[1].append(i)
        return answer