from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * 366
        dp[0] = 0
        j = 0
        for i in range(1, 366):
            if j < n and i == days[j]:
                dp[i] = min(dp[i], dp[i-1] + costs[0])
                dp[i] = min(dp[i], dp[i-7] + costs[1]) if i >= 7 else min(dp[i], costs[1])
                dp[i] = min(dp[i], dp[i-30] + costs[2]) if i >= 30 else min(dp[i], costs[2])
                j += 1
            else:
                dp[i] = dp[i-1]
        return dp[365]

solution = Solution()
print(solution.mincostTickets([1,4,6,7,8,20], [2,7,15]))

# Example 1:

# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total, you spent $11 and covered all the days of your travel.
# Example 2:

# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total, you spent $17 and covered all the days of your travel.
 

# Constraints:

# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000