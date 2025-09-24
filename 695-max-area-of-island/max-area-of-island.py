class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return 0
            if grid[i][j]==0:
                return 0
            grid[i][j]=0

            return 1+traverse(i+1,j)+traverse(i,j+1)+traverse(i-1,j)+traverse(i,j-1)


        rows=len(grid)
        cols=len(grid[0])
        area=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=max(area,traverse(i,j))
        
        return area