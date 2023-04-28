import bisect
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = l = len(nums)
        while start <= end:
            mid = (start + end) // 2 
            idx = bisect.bisect_left(nums, mid)
            if mid == l - idx:
                return mid
            elif l - idx < mid:
                end = mid - 1
            else:
                start = mid + 1
        return - 1

# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         l, r = 0, len(nums)

#         while l <= r:
#             m = (l+r)//2
#             c = sum(num >= m for num in nums)
#             if c == m:
#                 return m
#             if c > m:
#                 l = m+1
#             else:
#                 r = m-1
#         return -1


# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         c = {}
#         for x in range(len(nums)+1):
#             c[x] = 0
#             for num in nums:
#                 if num >= x:
#                     c[x] += 1
#         for i in c.keys():
#             if i == c[i]:
#                 return i
#         return -1


solution = Solution()
print(solution.specialArray([3,5])) # 2
print(solution.specialArray([0,0])) # -1
print(solution.specialArray([0,4,3,0,4])) # 3