
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        steps = nums[0]
        for i in range(1, n):
            if steps >= 1:
                steps = max(steps-1, nums[i])
            else:
                return False
        return True


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if n == 1:
#             return True
#         dp = [0] * (n+1)
#         dp[0] = nums[0]
#         for i in range(1, n):
#             if dp[i - 1] >= 1:
#                 dp[i] = max(dp[i-1]-1, nums[i])
#             else:
#                 return False
#         return True
    
sol = Solution()

print(sol.canJump([2,0,0])) #t
print(sol.canJump([2,3,1,1,4])) #t
print(sol.canJump([3,2,1,0,4])) #f