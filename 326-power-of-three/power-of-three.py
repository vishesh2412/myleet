import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        num=math.log(n,3)
        return(abs(round(num)-num)<1e-10)