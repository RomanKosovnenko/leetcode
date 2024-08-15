from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        
        def rob_solved(start: int, end: int) -> int:
            l1 = end-start
            dp = [0]*(l1+1)
            dp[1] = nums[start]
            dp[2] = max(dp[1],nums[start+1])
            for i in range(3, l1+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[start+i-1])
            return dp[l1]

        return max(rob_solved(0,l-1), rob_solved(1,l))
    
solution = Solution()
print(solution.rob([2,3,2])) # 3
print(solution.rob([1,2,3,1])) # 4