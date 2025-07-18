class Solution(object):
    def isAnagram(self, s, t):
        s1=list(s)
        t1=list(t)
        s1.sort()
        t1.sort()
        if s1==t1:
            return True
        return False