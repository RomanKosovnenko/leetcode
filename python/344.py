from typing import List


# class Solution: # 96%
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[::] = s[::-1]

# class Solution: # 98%
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i = 0
#         j = len(s) - 1
#
#         while i < j:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1

class Solution: # 99.86%
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()