class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        val=list(hash_map.values())

        return max(val)*(val.count(max(val)))