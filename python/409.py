from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hist = Counter(s)
        mid = 0 if all(cnt % 2 == 0 for cnt in hist.values()) else 1
        return mid + sum((cnt // 2) * 2 for cnt in hist.values())

sol = Solution()
print(sol.longestPalindrome("abcddcba")) # 7
print(sol.longestPalindrome("abcdfdcba")) # 7
print(sol.longestPalindrome("abccccdd")) # 7
print(sol.longestPalindrome("a")) # 1