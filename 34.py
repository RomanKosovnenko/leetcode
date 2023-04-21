from typing import List
from bisect import bisect_left, bisect_right, bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(l, r):
            while l<=r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
        n = len(nums)
        idx = search(0, n-1)
        if idx == -1:
            return [-1, -1]
        ans = []
        while idx>= 0 and idx < n and nums[idx] == target:
            idx -=1
        idx +=1
        ans.append(idx)
        while idx>= 0 and idx < n and nums[idx] == target:
            idx +=1
        idx -=1
        ans.append(idx)
        return ans
    
sol = Solution()
print(sol.searchRange(nums = [], target = 0)) # [-1 -1]
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6)) # [-1 -1]
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8)) # [3 4]
print(sol.searchRange(nums = [1], target = 1)) # [0 0]
print(sol.searchRange(nums = [1, 3], target = 1)) # [0 0]