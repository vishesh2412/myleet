class Solution(object):
    def isPalindrome(self, s):
        ans=''
        for i in s:
            if i.isalnum()==True:
                ans+=i.lower()
        return ans==ans[::-1]