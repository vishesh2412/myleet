from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[float('inf')]*(n + 1)
        dp[n-1]=0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[j]=grid[i][j]+min(dp[j],dp[j+1])
        return dp[0]