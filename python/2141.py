class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        for i in range(n):
            if batteries[i] <= i:
                return i
        return n


solution = Solution()
print(solution.maxRunTime(3, [3, 3, 3]))
