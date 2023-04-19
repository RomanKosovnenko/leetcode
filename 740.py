from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        values = [0] * (m+1)
        for num in nums:
            values[num] += num

        if len(values) <= 2:
            return max(values)
        dp = [0] * (m+1)
        dp[1] = values[1]
        dp[2] = values[2]
        for i in range(2, len(values)):
            dp[i] = max(dp[i-1], dp[i-2]+values[i])
        return dp[-1]



solution = Solution()
print(solution.deleteAndEarn([3,4,2])) # 6
print(solution.deleteAndEarn([2,2,3,3,3,4])) # 9
print(solution.deleteAndEarn([1,1,1,2,4,5,5,5,6])) # 18