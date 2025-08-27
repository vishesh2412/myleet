class Solution:
    def checkString(self, s: str) -> bool:
        n=len(s)
        i=0
        flag=0
        while(i<n):
            if s[i]=='a' and flag==1:
                return False
            if s[i]=='b':
                flag=1
            i+=1
        return True
                    
            
