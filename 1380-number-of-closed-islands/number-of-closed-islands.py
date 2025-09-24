class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            if grid[r][c] == 1:
                return True
            
            grid[r][c] = 1  # mark as visited
            
            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            
            return top and bottom and left and right
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1
        return count
