class Solution(object):
    def groupAnagrams(self, strs):
        new=[]
        dict1=defaultdict(list)
        for i in strs:
            form=''.join(sorted(i))
            dict1[form].append(i)
        output = list(dict1.values())
        return output