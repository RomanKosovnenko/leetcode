# The isBadVersion API is already defined for you.
bad = 5
def isBadVersion(version: int) -> bool:
    return version >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n-1

        while l <= r:
            m = (l+r)//2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m - 1
        return l

sol = Solution()

print(sol.firstBadVersion(5))
