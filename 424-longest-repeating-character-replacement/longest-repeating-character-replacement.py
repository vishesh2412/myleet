class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        length=len(s)
        count={}
        max_freq=0
        ans=0
        while(j<length):
            ch=s[j]
            count[ch]=count.get(ch,0)+1
            max_freq=max(max_freq,count[ch])
            while(j-i+1-max_freq)>k:
                count[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans
