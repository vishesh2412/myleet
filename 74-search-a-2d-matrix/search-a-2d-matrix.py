class Solution(object):
    def searchMatrix(self, matrix, target):
        length=len(matrix[0])
        for i in matrix:
            if target>i[-1]:
                continue
            elif target in i:
                return True
        return False                