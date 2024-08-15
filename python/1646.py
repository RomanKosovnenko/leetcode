class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1: return n
        nums = [0] *(n+1)
        nums[1] = 1
        i = 1
        maxv = 1
        while 2*i <= n and 2*i+1 <= n:
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
            maxv = max(maxv,nums[2 * i], nums[2 * i + 1])
            i += 1
        return maxv
