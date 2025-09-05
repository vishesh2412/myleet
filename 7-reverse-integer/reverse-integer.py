class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        num=0
        while(x>0):
            num+=(x%10)
            num*=10
            x=x//10
        result=num//10
        if(result < -2**31 or result > 2**31 - 1):
            return 0
        return result*sign