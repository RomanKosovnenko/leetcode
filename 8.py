class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1 if s[0] != "-" else -1
        if s[0] in ["+", "-"]:
            s = s[1:]
        i = 0
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        if res < -2**31:
            return -2**31
        if res > 2**31-1:
            return 2**31-1
        return res

solution = Solution()
print(solution.myAtoi(".1"))
print(solution.myAtoi(""))
