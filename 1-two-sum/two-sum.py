class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}

        for i,num in enumerate(nums):
            c=target-num

            if c in hash_map:
                return [i,hash_map[c]]
            
            hash_map[num]=i
            
