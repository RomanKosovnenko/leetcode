import math
from typing import List


# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         def print_matrix():
#             for row in matrix:
#                 print(row)
#             print()
#
#         n = len(matrix)-1
#         print_matrix()
#         for i in range(len(matrix)//2):
#             matrix[n - i][n - i], matrix[i][n - i], matrix[i][i], matrix[n - i][i] = \
#             matrix[i][n - i], matrix[i][i], matrix[n - i][i], matrix[n - i][n - i]
#             # print_matrix()
#             for j in range(i+1, n-i):
#                 # print(f"j={j}")
#                 matrix[i][n - j], matrix[j][i],   matrix[n - i][j], matrix[n-j][n-i] = \
#                 matrix[j][i],     matrix[n-i][j], matrix[n-j][n-i], matrix[i][n - j]
#                 # print_matrix()
#
#         print_matrix()
#         return matrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for item in matrix:
            item.reverse()

solution = Solution()
print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
print(solution.rotate([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]) == [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]])

