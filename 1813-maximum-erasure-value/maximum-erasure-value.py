class Solution(object):
    def maximumUniqueSubarray(self, nums):
        window=[]
        total=0
        for i in nums:
            if i in window:
                total=max(total,sum(window))
                j=window.index(i)
                window=window[j+1:]
                window.append(i)
            else:
                window.append(i)
        return max(total,sum(window))