class Solution(object):
    def hammingWeight(self, n):
        n=str(bin(n))
        return n.count('1')