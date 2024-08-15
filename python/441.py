class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         l, r = 0, n
#         while l <= r:
#             m = (l+r)//2
#             curr = m * (m + 1) // 2
#             if curr == n:
#                 return m
#             if n < curr:
#                 r = m - 1
#             else:
#                 l = m + 1
#         return r

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         k = 0
#         ans = 0
#         while n > 0:
#             k += 1
#             if n >= k:
#                 ans += 1
#             n -= k
#         return ans

solution = Solution()
print(solution.arrangeCoins(5)) # 2
print(solution.arrangeCoins(8)) # 3