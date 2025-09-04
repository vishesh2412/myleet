class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 0 if (z-x)**2 == (z-y)**2 else (1 if (z-x)**2 < (z-y)**2 else 2)
