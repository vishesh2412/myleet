class Solution(object):
    def groupAnagrams(self, strs):
        output={}
        for i in strs:
            check=tuple(sorted(i))
            if check in output:
                output[check].append(i)
            else:
                output[check]=[i]
        return output.values()