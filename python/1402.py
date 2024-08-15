from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dp = [[0]*(len(satisfaction)+1) for _ in range(len(satisfaction)+1)]
        satisfaction.sort()
        for i in range(1, len(satisfaction)+1):
            ll = satisfaction[i-1:] + satisfaction[:i-1]
            t = 1
            for j in range(1, len(satisfaction)+1):
                m = max(dp[i][j-1], dp[i-1][j])
                new_value = m + t * ll[j-1]
                if new_value > m:
                    dp[i][j] = new_value
                    t += 1
                else:
                    dp[i][j] = m
        return 1

sol = Solution()
print(sol.maxSatisfaction([-1,-8,0,5,-9])) # 14
print(sol.maxSatisfaction([4,3,2])) # 20
print(sol.maxSatisfaction([-1,-4,-5])) # 0