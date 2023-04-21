from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        row = l-1

        l = 0
        r = m-1
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False
    
sol = Solution()
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)) # t
print(sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)) # f
# print(sol.searchMatrix("abccccdd")) # 7
# print(sol.searchMatrix("a")) # 1
