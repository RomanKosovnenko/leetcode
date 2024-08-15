from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k

solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))