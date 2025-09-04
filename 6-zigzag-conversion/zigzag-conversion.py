class Solution(object):
    def convert(self, s, numRows):
        answer=['']*numRows
        i=0
        j=0
        while(i<len(s)):
            if j<numRows:
                answer[j]+=s[i]
                i+=1
                j+=1
            else:
                for k in range(numRows-2):
                    if i<len(s):
                        answer[numRows-k-2]+=s[i]
                        i+=1
                j=0
        return ''.join(answer)