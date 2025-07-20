class Solution(object):
    def isHappy(self, n):
        answer=set()
        while n!=1:
            if n in answer:
                return False
            answer.add(n)
            n=sum(int(digit)**2 for digit in str(n))
        return True