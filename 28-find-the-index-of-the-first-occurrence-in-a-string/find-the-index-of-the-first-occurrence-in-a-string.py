class Solution(object):
    def strStr(self, haystack, needle):
        if needle=="":
            return 0
        check=len(haystack)-len(needle)+1
        for i in range(check):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
