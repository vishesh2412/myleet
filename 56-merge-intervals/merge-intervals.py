class Solution(object):
    def merge(self, intervals):
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            if ans==[] or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            # elif ans[-1][1]>intervals[i][0]:
            else:
                ans[-1][0]=min(ans[-1][0],intervals[i][0])
                ans[-1][1]=max(ans[-1][1],intervals[i][1])    
        return ans