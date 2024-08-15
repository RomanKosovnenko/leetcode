from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, v in enumerate(nums):
            if target - v in check:
                return [i, check[target - v]]
            check[v] = i