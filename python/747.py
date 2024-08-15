from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mi = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[mi]:
                mi = i
        si=0 if mi != 0 else 1
        for i in range(len(nums)):
            if i != mi and nums[i] > nums[si]:
                si = i
        if nums[mi] >= 2* nums[si]:
            return mi
        else:
            return -1

    def dominantIndex2(self, nums: List[int]) -> int:
        first = idx = second = 0
        for i, val in enumerate(nums):
            if val > first:
                second = first
                idx = i
                first = val
            elif val > second:
                second = val
        return idx if first >= 2* second else -1

    def dominantIndexpy(self, nums: List[int]) -> int:
        val = max(nums)
        idx = nums.index(val)
        nums.pop(idx)
        return idx if val >= max(nums) * 2 else -1

sol = Solution()

print(sol.dominantIndexpy([3,6,1,0])) #1
print(sol.dominantIndexpy([1,2,3,4])) #-1
print(sol.dominantIndexpy([0,0,3,2])) #-1
print(sol.dominantIndexpy([1,0])) #0
print(sol.dominantIndexpy([0,0,0,1])) #3