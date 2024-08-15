from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l

sol = Solution()

print(sol.searchInsert([1,3,5,6], 5)) #2
print(sol.searchInsert([1,3,5,6], 2)) #1
print(sol.searchInsert([1,3,5,6], 7)) #4
print(sol.searchInsert([1,3,5,6], 0)) #0
