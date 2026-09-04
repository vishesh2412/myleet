class Solution(object):
    def merge(self, intervals):
        ans=[]
        intervals.sort()
        for i in intervals:
            if ans==[] or ans[-1][1]<i[0]:
                ans.append(i)
            else:
                ans[-1][0]=min(ans[-1][0],i[0])
                ans[-1][1]=max(ans[-1][1],i[1])    
        return ans