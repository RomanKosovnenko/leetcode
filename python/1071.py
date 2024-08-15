# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if len(str1) < len(str2):
#             str1, str2 = str2, str1
        
#         i = len(str2)

#         while i > 0:
#             if len(str1) % i == 0 and len(str2) % i == 0:
#                 prefix = str2[:i]
#                 if prefix * (len(str1) // i) == str1 and prefix * (len(str2) // i) == str2:
#                     return str1[:i]
#             i -= 1
#         return ""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return j+1 if j != 0 else 0
    
s = Solution()
# print(s.removeElement([3,2,2,3], 3)) #2
print(s.removeElement([1], 1)) #2