
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])
            if i == cur_end:
                answer += 1
                cur_end = cur_far

        return answer

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return 0
#         dp = [0]*n

#         for i, num in enumerate(nums):
#             for j in range(1,num+1):
#                 if dp[i+j] == 0:
#                     dp[i+j] = dp[i]+1
#                 if dp[n-1] != 0:
#                     return dp[-1]

#         return dp[-1]
    
sol = Solution()
print(sol.jump([2,3,1,1,4])) #2
print(sol.jump([3,2,0,1,4])) #2
print(sol.jump([2,0,0])) #1
print(sol.jump([1])) #0