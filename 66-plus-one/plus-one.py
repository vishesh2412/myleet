class Solution(object):
    def plusOne(self, digits):
        a=''
        for i in digits:
            a+=str(i)
        b=str(int(a)+1)
        ans=[]
        for i in b:
            ans.append(int(i))
        return ans        