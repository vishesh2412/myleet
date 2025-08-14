class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i=0
        ans=""
        while i<=9:
            check=str(i)*3
            if check in num:
                ans=check
            i+=1
        return ans