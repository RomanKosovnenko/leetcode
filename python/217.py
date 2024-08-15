from typing import List


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) > len(set(nums))

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 return True
#             i += 1
#         return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            d[nums[i]] = 1
        return False