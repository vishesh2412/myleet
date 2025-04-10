class Solution(object):
    def largestAltitude(self, gain):
        height=0
        max=0
        for i in gain:
            height+=i
            if(height>max):
                max=height

        return max