class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split()
        b=len(a[-1])
        return b