class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return 2**31-1 if dividend==-2**31 and divisor==-1 else int(dividend/divisor)
        