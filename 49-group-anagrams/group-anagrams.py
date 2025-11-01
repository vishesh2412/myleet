class Solution(object):
    def groupAnagrams(self, strs):
        check = {}
        for i in strs:
            key = ''.join(sorted(i))
            check.setdefault(key, []).append(i)
        return list(check.values())
