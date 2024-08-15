from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        dp = [0]*(l+1)
        dp[1] = nums[0]
        dp[2] = max(dp[1],nums[1])
        for i in range(3, l+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        return dp[l]

solution = Solution()
print(solution.rob([2,1,1,2])) # 4