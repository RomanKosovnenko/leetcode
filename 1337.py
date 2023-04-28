from typing import List
from collections import Counter

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l_row = len(mat[0])
        def binary(row):
            l,r=0,l_row-1
            while l<=r:
                m=(r+l)//2
                if row[m]==1:
                    l=m+1
                else:
                    r=m-1
            return l
        list1=[]
        for ind,row in enumerate(mat):
            list1.append([binary(row),ind])
        list1.sort(key=lambda x:x[0])
        return [list1[i][1] for i in range(k)]

# class Solution:
# 	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
# 		m = len(mat)
# 		rows = sorted(range(m), key=lambda i: (mat[i], i))
# 		return rows[:k]

# class Solution:
# 	def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
# 		id_1count = [[row.count(1),ind] for ind, row in enumerate(mat)]
# 		id_1count.sort(key=lambda x: x[0])
# 		return [id_1count[i][1] for i in range(k)]

solution = Solution()
print(solution.kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)) # [2,0,3]
print(solution.kWeakestRows(mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2)) # [0,2]