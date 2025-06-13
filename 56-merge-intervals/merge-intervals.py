class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]<=result[-1][1]:
                result[-1][1]=max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
        return result