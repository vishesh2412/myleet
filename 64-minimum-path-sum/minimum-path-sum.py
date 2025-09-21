class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[float('inf')]*(n + 1) for _ in range(m+1)]
        dp[m-1][n]=0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]