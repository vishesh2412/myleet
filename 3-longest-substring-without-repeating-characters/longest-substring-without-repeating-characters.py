class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=set()
        max_len=0
        left=0

        for right in range(len(s)):
            while s[right] in count:
                count.remove(s[left])
                left+=1

            max_len=max(max_len,right-left+1)
            count.add(s[right])

        return max_len        
