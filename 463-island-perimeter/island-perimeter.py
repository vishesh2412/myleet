class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        final=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]==0:
                        final+=1
                    if i==n-1 or grid[i+1][j]==0:
                        final+=1
                    if j==0 or grid[i][j-1]==0:
                        final+=1
                    if j==m-1 or grid[i][j+1]==0:
                        final+=1
        return final