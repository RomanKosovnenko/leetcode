from typing import List
from collections import Counter

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         loop1 = Counter(nums1)
#         res = []
#
#         for num in nums2:
#             if loop1[num]>0:
#                 res.append(num)
#                 loop1[num] -= 1
#         return res


# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         loop1, loop2 = Counter(nums1), Counter(nums2)
#         res = []

#         for key in loop1:
#             if key in loop2:
#                 res.extend([key]*min(loop1[key], loop2[key]))
#         return res


# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         if len(nums1) > len(nums2):
#             return self.intersect(nums2, nums1)
#         ans = []
#         i = 0
#         while i < len(nums1):
#             if nums1[i] in nums2:
#                 ans.append(nums1[i])
#                 nums2.remove(nums1[i])
#             i += 1
#         return ans

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        loop1 = {}
        for num in nums1:
            if num in loop1:
                loop1[num] += 1
            else:
                loop1[num] = 1
        res = []

        for num in nums2:
            if num in loop1 and loop1[num] > 0:
                res.append(num)
                loop1[num] -= 1
        return res

solution = Solution()
print(solution.intersect([1,2,2,1], [2,2])) # [2,2]
print(solution.intersect([4,9,5], [9,4,9,8,4])) # 4,9 or 9,4
