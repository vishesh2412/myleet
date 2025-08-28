class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==2 or x==3:
            return 1
        if x==5:
            return 2
        for i in range(int(x/2)+1):
            if i**2>x:
                return i-1
            elif i**2==x:
                return i