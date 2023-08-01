from typing import List


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         l = 0
#         r = 1
#
#         while r < len(nums):
#             if nums[l] == nums[r] and l != r:
#                 l += 1
#                 r = 0
#             else:
#                 r += 1
#         return nums[l]


# class Solution:
#
#     def singleNumber(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         l = 0
#         r = 1
#
#         while l < r and r < len(nums):
#             if nums[l] == 99999:
#                 l += 1
#                 r = l + 1
#                 continue
#             if nums[r] == 99999:
#                 r += 1
#                 continue
#             if nums[l] == nums[r]:
#                 nums[l] = 99999
#                 nums[r] = 99999
#                 l += 1
#                 r = l + 1
#             else:
#                 r += 1
#         return nums[l]

# class Solution:
#
#     def singleNumber(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         nums.sort()
#         l = 0
#         r = 1
#
#         while l < r and r < len(nums):
#             if nums[l] == nums[r]:
#                 l += 2
#                 r += 2
#             else:
#                 return nums[l]
#         return nums[l]

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for val in nums[1:]:
            ans ^= val
        return ans