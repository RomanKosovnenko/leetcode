# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.index(needle) if needle in haystack else -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         m, n = len(haystack), len(needle)
#         return next((i for i in range(m-n+1) if haystack[i:i+n] == needle), -1)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         m, n = len(haystack), len(needle)
#         for i in range(0, m-n+1):
#             if haystack[i:i+n] == needle:
#                 return i
#         return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1