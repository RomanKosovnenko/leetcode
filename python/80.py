from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        f = 0
        s = 1
        while s+1 < len(nums):
                if nums[f] == nums[s] and nums[f] == nums[s+1]:
                   nums.pop(s+1)
                else:
                    f += 1
                    s += 1
        return len(nums)

solution = Solution()
print(solution.removeDuplicates([1,1,1,2,2,3])) #5
print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3])) #7


