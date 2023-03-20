from ast import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        if len(profits) == 0:
            return profits[0] if capital[0] <= w else capital
        projects = sorted(zip(capital, profits), reverse=True)

        maxProfit = []

        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heappush(maxProfit, -projects.pop()[1])
            if maxProfit:
                w -= heappop(maxProfit)
        return w
            

            
sol = Solution()

print(sol.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))
print(sol.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))