from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*(m) for _ in range(n)]
        dp[0][0]= grid[0][0]
        for i in range(1,m):
            dp[0][i] = dp[0][i-1]+grid[0][i]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1,n):
            for j in range (1, m):
                dp[i][j] = min(dp[i-1][j],  dp[i][j-1]) + grid[i][j]
        return dp[n-1][m-1]

solution = Solution()
print(solution.minPathSum([[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]))