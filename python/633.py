import bisect
import itertools
import math
from typing import List

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
        #   m = l**2 + r**2
          m = (l * l) + (r * r)
          if m == c :
            return True
          if m > c:
            r -= 1
          else:
            l += 1
        return False

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         for a in range(int(math.sqrt(c))+1):
#             l, r = 0, c
#             while l <= r:
#                 b = (l+r)//2
#                 t = a*a+b*b
#                 if t==c:
#                     return True
#                 if t > c:
#                     r = b-1
#                 else:
#                     l = b+1
#         return False

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         def bs(l,r,n):
#             if l > r:
#                 return False
#             m = (l+r)//2
#             t = m**2
#             if t == n:
#                 return True
#             return bs(l, m-1, n) if t > n else bs(m+1, r, n)

#         for a in range(int(math.sqrt(c))+1):
#             b = c-a**2
#             if bs(0,b,b):
#                 return True
#         return False

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         for a in range(int(math.sqrt(c))+1):
#             b = math.sqrt(c-a**2)
#             if b == int(b):
#                 return True
#         return False

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         squares = []
#         i = 0
#         while i**2 <= c:
#             squares.append(i**2)
#             i += 1
        
#         for a in range(len(squares)):
#             b = bisect.bisect_left(squares, c-squares[a])
#             if b !=len(squares) and squares[b] == c-squares[a]:
#                 return True
#         return False

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         for a in range(c+1):
#             for b in range (c+1):
#                 t = a*a + b*b
#                 if t > c:
#                     break
#                 if t == c:
#                     return True
#         return False


# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         return any(
#             a * a + b * b == c
#             for a, b in itertools.product(range(c + 1), range(c + 1))
#         )

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         for a in range(c+1):
#             for b in range (c+1):
#                 if a*a + b*b == c:
#                     return True
#         return False


solution = Solution()
print(solution.judgeSquareSum(5)) # t
print(solution.judgeSquareSum(5)) # t
print(solution.judgeSquareSum(3)) # f