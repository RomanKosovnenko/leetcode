from collections import Counter


# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         counter = {}
#         for i in range(len(s)):
#             if s[i] not in counter:
#                 counter[s[i]] = i
#             else:
#                 counter.pop(s[i])
#
#         if counter:
#             return counter.popitem()[1]
#         return 0
#
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         counter = {}
#         for i in range(len(s)):
#             if s[i] not in counter:
#                 counter[s[i]] = [1,i]
#             else:
#                 counter[s[i]][0] += 1
#         return min([val[1][1] for val in counter.items() if val[1][0] == 1], default=-1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

solution = Solution()
print(solution.firstUniqChar("leetcode"))
print(solution.firstUniqChar("loveleetcode"))
print(solution.firstUniqChar("aabb"))
