class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n+1)

        for i in range(1, n+1):
            steps[i] = i if i < 3 else (steps[i-1]) + steps[i-2]
        return steps[n]