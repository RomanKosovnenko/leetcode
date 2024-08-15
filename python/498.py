from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        N = len(mat)
        M = len(mat[0])
        row, column = 0, 0
        arr = []
        isUpwards = True

        while row < N and column < M:

            arr.append(mat[row][column])

            new_i = row + (-1 if isUpwards else 1)
            new_j = column + (1 if isUpwards else -1)

            if new_i < 0 or new_i == N or new_j < 0 or new_j == M:
                if isUpwards:
                    row += (column == M - 1)
                    column += (column < M -1)
                else:
                    column += (row == N -1)
                    row += (row < N - 1)
                isUpwards = not isUpwards
            else:
                row = new_i
                column = new_j
        return arr

sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])) #[1,2,4,7,5,3,6,8,9]
print(sol.findDiagonalOrder([[1,2],[3,4]])) #[1,2,3,4]