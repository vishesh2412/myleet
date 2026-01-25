class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        x_val=[]
        y_val=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    x_val.append(i)
                    y_val.append(j)
        
        for i in x_val:
            matrix[i]=[0]*m
        for i in y_val:
            for j in range(n):
                matrix[j][i]=0
        