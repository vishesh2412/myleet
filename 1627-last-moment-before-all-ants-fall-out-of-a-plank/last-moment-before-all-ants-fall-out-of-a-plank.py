class Solution(object):
    def getLastMoment(self, n, left, right):
        if left and right:
            return max(max(left),n-min(right))
        elif left:
            return max(left)
        else:
            return n-min(right)