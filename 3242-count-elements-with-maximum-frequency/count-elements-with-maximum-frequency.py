class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=Counter(nums).values()
        return max(freq)*list(freq).count(max(freq))