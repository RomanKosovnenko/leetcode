class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        l, r = 0, num-1

        while l <= r:
            m = (l+r)//2
            m2 = m**2
            if m2 == num:
                return True
            if m2 > num:
                r = m-1
            else:
                l = m+1
        return False
    
solution = Solution()
print(solution.isPerfectSquare(16)) # T
print(solution.isPerfectSquare(14)) # F
print(solution.isPerfectSquare(1)) # T