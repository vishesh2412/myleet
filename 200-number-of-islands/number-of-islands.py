class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return 
            if grid[i][j]=='0':
                return 
            grid[i][j]='0'

            traverse(i+1,j)
            traverse(i,j+1)
            traverse(i-1,j)
            traverse(i,j-1)

        rows=len(grid)
        cols=len(grid[0])
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count+=1
                    traverse(i,j)
        
        return count