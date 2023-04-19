from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix)
        m = len(matrix[0])
        fr, lc, lr, fc = 0, m-1, n-1, 0

        for j in range(n+m-1):
            match (j % 4):
                case (0):
                    res.extend(matrix[fr][i] for i in range(fc, lc + 1))
                    fr += 1
                case (1):
                    res.extend(matrix[i][lc] for i in range(fr, lr + 1))
                    lc -= 1
                case (2):
                    res.extend(matrix[lr][i] for i in range(lc, fc - 1, -1))
                    lr -= 1
                case (3):
                    res.extend(matrix[i][fc] for i in range(lr, fr - 1, -1))
                    fc += 1
            if fr > lr or fc > lc:
                break
        return res


solution = Solution()
print(solution.spiralOrder([[6,9,7]])) # [6,9,7]
print(solution.spiralOrder([[1,2,3],
                            [4,5,6],
                            [7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(solution.spiralOrder([[1,2, 3, 4],
                            [5,6, 7, 8],
                            [9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]