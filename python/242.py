from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isAnagram(t,s)
        c1 = Counter(s)
        c2 = Counter(t)

        c3 = c1-c2
        return not c3

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) < len(t):
#             return self.isAnagram(t,s)
#         c1 = {}
#         for char in s:
#             if char not in c1:
#                 c1[char] = 1
#             else:
#                 c1[char] += 1
#         for char in t:
#             if char not in c1:
#                 return False
#             if c1[char] == 1:
#                 c1.pop(char)
#             else:
#                 c1[char] -= 1
#         return not c1

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
print(solution.isAnagram("a", "ab"))
