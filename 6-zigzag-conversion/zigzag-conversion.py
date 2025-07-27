class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        answer=['']*numRows
        ind=0
        direction=1
        for i in s:
            answer[ind]+=i
            if ind==0:
                direction=1
            elif ind==numRows-1:
                direction=-1
            ind+=direction
        return ''.join(answer)