class Solution:
    def reverseBits(self, n: int) -> int:
        binary=format(n,'032b')
        new=binary[::-1]
        return int(new,2)
