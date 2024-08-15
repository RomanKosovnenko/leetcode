# class Solution:
#     def reverse(self, x: int) -> int:
#         l = []
#         is_minus = 1
#         if x < 0:
#             is_minus = -1
#             x *= -1
#         num = 0
#         while x > 0:
#             l.append(str(x % 10))
#             x //= 10
#         if l:
#             num = "".join(l)
#             num = int(num)
#         return 0 if num > 2**31 -1 else is_minus * num

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1

        x *= sign

        while x != 0:
            res = res*10 + x % 10
            x //=10
        if sign * res < -2 ** 31 or sign * res > 2 ** 31 - 1:
            return 0
        return sign * res

solution = Solution()
print(solution.reverse(0))
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
