class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def traverse(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0:
                return 0
            a=grid[i][j]
            grid[i][j]=0

            return a+traverse(i+1,j)+traverse(i,j+1)+traverse(i-1,j)+traverse(i,j-1)


        n=len(grid)
        m=len(grid[0])
        count=0

        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    if traverse(i,j)%k==0:
                        count+=1
        
        return count