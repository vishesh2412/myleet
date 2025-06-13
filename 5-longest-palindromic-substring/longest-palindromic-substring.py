class Solution(object):
    def longestPalindrome(self, s):
        def comeagain(left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            return s[left+1:right]
        
        answer=''
        for i in range(len(s)):
            o=comeagain(i,i)
            e=comeagain(i,i+1)
            if(len(o)>len(answer)):
                answer=o
            if(len(e)>len(answer)):
                answer=e
        return answer