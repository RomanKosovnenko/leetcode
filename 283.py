from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = 0
#         r = 1
#         while l < len(nums):
#             if nums[l] != 0:
#                 l += 1
#                 r = l + 1
#                 continue
#             else:
#                 while r < len(nums):
#                     if nums[r] != 0:
#                         nums[l], nums[r] = nums[r], nums[l]
#                         break
#                     else:
#                         r += 1
#                 l += 1
#                 r += 1
#         return nums