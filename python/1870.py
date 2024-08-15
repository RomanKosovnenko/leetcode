from math import ceil
from typing import List


# class Solution:
#     def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
#         l = 0
#         r = 10**7
#         speed = 0
#         t = 0
#         while l <= r:
#             if l == r and l == speed:
#                 return speed
#             speed = (l+r)//2
#             if speed == 0:
#                 return r
#             t = 0
#             for i in range(len(dist)):
#                 t = ceil(t)
#                 t += dist[i]/speed
#                 if t > hour:
#                     l = speed + 1
#                     break
#                 elif i == len(dist)-1:
#                     r = speed
#         return -1

# class Solution:
#     def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
#         l = 1
#         r = 2
#         speed = 0
#         t = 0
#         while l <= r:
#             if l == r and l == speed:
#                 return speed
#             speed = (l+r)//2
#             if speed == 0:
#                 return r
#             t = 0
#             for i in range(len(dist)):
#                 t = ceil(t)
#                 t += dist[i]/speed
#                 if t > hour:
#                     if r != 10**7:
#                         if r*2 >= 10**7:
#                             r = 10**7
#                         else:
#                             r *= 2
#                     l = speed + 1
#                     break
#                 elif i == len(dist)-1:
#                     r = speed
#         return -1
    
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        r = 10**7
        min_speed = -1

        def calc_time(speed):
            t = 0
            for i in range(len(dist)):
                t = ceil(t)
                t += dist[i]/speed
            return t

        while l <= r:
            speed = (l+r)//2
            
            if (calc_time(speed) <= hour):
                min_speed = speed
                r = speed - 1
            else:
                l = speed + 1
        return min_speed

solution = Solution()
print(solution.minSpeedOnTime([1,3,2], 6))
print(solution.minSpeedOnTime([1,3,2], 2.7))
print(solution.minSpeedOnTime([1,3,2], 1.9))
print(solution.minSpeedOnTime([1,1,100000], 2.01))