class Solution(object):
    def groupAnagrams(self, strs):
        check={}
        for i in strs:
            stri=''.join(sorted(i))
            if stri in check:
                check[stri].append(i)
            else:
                check[stri]=[i]
        return list(check.values())