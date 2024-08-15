from typing import List


# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         l, r = 0, len(arr)-1

#         while l<r:
#             m = (l+r)//2

#             if arr[m] < arr[m + 1]:
#                 l = m + 1
#             else:
#                 r = m
#         return l

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l <= r:
            m = (l+r)//2
            if m != 0 and arr[m-1] > arr[m]:
                r = m-1
            elif arr[m] < arr[m+1]:
                l = m+1
            else:
                return m

solution = Solution()
#print(solution.peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
print(solution.peakIndexInMountainArray([3,9,8,6,4]))