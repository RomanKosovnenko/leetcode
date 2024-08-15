class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            m = (l+r)//2

            t = m*m
            if t == x:
                return m
            if t > x:
                r = m-1
            else:
                l = m+1
        return l-1

sol = Solution()

print(sol.mySqrt(1))
print(sol.mySqrt(2))
print(sol.mySqrt(4))
print(sol.mySqrt(8)) #2
print(sol.mySqrt(9)) #2
print(sol.mySqrt(25)) #2
print(sol.mySqrt(225)) #2
print(sol.mySqrt(250)) #2