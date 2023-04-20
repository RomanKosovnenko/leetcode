from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r_num = len(mat)
        c_num = len(mat[0])
        if r_num*c_num != r*c:
            return mat
        flat,ans=[],[]
        for i in mat:
            flat+=i
        for i in range(r):
            ans+=[flat[i*c:i*c+c]]
        return ans