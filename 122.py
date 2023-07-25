# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         i = 0
#         while i < len(prices)-1:
#             ans += prices[i+1]-prices[i] if prices[i+1]-prices[i] > 0 else 0
#             i += 1
#         return ans

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         i = 0
#         while i < len(prices)-1:
#             ans += max(prices[i+1]-prices[i], 0)
#             i += 1
#         return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(prices)-1:
            if prices[i+1]-prices[i] > 0:
                ans += prices[i+1]-prices[i]
            i += 1
        return ans
