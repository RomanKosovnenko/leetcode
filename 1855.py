from typing import List
import bisect

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        ans = 0
        nums2.reverse()
        for i in range(l1):
            k = bisect.bisect_left(nums2, nums1[i])
            ans = max(ans, l2 - k - 1 - i)
        return ans

# class Solution:
#     def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
#         l2 = len(nums2)
#         def search(l, value):
#             r = l2-1
#             while l <= r:
#                 m = (l+r)//2
#                 if nums2[m] == value:
#                     return m
#                 if nums2[m] < value:
#                     r = m - 1
#                 else:
#                     l = m +1
#             if nums2[r] >= value:
#                 return r
#             return -1
#         ans = []
#         for i in range(len(nums1)):
#             if i >= l2:
#                 break
#             idx = search(i, nums1[i])
#             if idx != -1 and idx >= i:
#                 ans.append(idx-i)
#         return max(ans) if len(ans)>0 else 0



solution = Solution()
print(solution.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5])) # 2
print(solution.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1])) # 1
print(solution.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25])) # 2
print(solution.maxDistance(nums1 = [5,4], nums2 = [3,2])) # 0