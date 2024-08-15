import bisect
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0
        for row in grid:
            l, r = 0, n-1
            while l <= r:
                m = (l + r) // 2
                if (row[m]) >= 0:
                    l = m + 1
                else:
                    r = m -1
            ans += n-l
        return ans

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         ans = 0
#         for i in range(n):
#             idx = bisect.bisect_left(grid[i][::-1], 0)
#             ans += idx
#         return ans


solution = Solution()
print(solution.countNegatives([[3,2],[1,0]])) # 0
print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8