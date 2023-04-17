from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum
