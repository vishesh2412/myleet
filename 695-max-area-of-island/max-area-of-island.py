class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0:
                return 0
            grid[i][j]=0

            return 1+traverse(i+1,j)+traverse(i,j+1)+traverse(i-1,j)+traverse(i,j-1)


        n=len(grid)
        m=len(grid[0])
        area=0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    area=max(area,traverse(i,j))
        
        return area