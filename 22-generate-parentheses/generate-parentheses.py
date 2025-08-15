class Solution(object):
    def generateParenthesis(self, n):
        answer=[]
        def recurse(open_count,close_count,string):
            if len(string)==2*n:
                answer.append(string)
                return
            if open_count<n:
                recurse(open_count+1,close_count,string+'(')
            if close_count<open_count:
                recurse(open_count,close_count+1,string+')')
            
        recurse(0,0,'')
        return answer
