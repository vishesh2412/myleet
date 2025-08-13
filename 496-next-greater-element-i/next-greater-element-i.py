class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer=[]
        for i in nums1:
            flag=1
            for j in nums2[nums2.index(i):]:
                if j>i:
                    answer.append(j)
                    flag=0
                    break
            if flag==1:
                answer.append(-1)
        return answer