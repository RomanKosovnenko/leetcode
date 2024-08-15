from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            ans.append([])
            for j in range(i + 1):
                if j in [0, i]:
                    ans[i].append(1)
                else:
                    a = ans[i - 1][j - 1] + ans[i - 1][j]
                    ans[i].append(a)
        return ans