class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash_map=set(nums)
        # if not nums:
        #     return 0
        # longest=1

        # for i in hash_map:
        #     if i-1 not in hash_map:
        #         length=1
        #         while i+length in hash_map:
        #             length+=1
        #         longest=max(longest,length)

        # return longest
                
        my_set=sorted(list(set(nums)))
        i=0
        j=0
        if not nums:
            return 0
        longest=1
        n=len(my_set)
        while(j+1<n):
            if my_set[j]+1==my_set[j+1]:
                j+=1
                length=j-i+1
                longest=max(longest,length)
            else:
                j+=1
                i=j
        return longest