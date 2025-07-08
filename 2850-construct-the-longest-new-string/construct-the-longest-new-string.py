class Solution(object):
    def longestString(self, x, y, z):
        if x>y:
            return 2*(z+2*y+1)
        elif y>x:
            return 2*(2*x+1+z)
        else:
            return 2*(z+2*x)