class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid2[i][j]==0:
                return True
            grid2[i][j]=0

            fine=grid1[i][j]==1

            fine&=traverse(i+1,j)
            fine&=traverse(i,j+1)
            fine&=traverse(i-1,j)
            fine&=traverse(i,j-1)

            return fine

        n=len(grid1)
        m=len(grid1[0])
        count=0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    if traverse(i,j):
                        count+=1
        return count