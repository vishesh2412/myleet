class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=rows or j>=cols:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1

            top=traverse(i,j-1)
            bottom=traverse(i,j+1)
            left=traverse(i-1,j)
            right=traverse(i+1,j)

            return top and bottom and left and right

        rows=len(grid)
        cols=len(grid[0])
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    if traverse(i,j):
                        count+=1
        
        return count