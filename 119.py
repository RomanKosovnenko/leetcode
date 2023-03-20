from typing import List


class Solution:
    def getRow1(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex):
            ans.append([])
            for j in range(i + 1):
                if j in [0, i]:
                    ans[i].append(1)
                else:
                    a = ans[i - 1][j - 1] + ans[i - 1][j]
                    ans[i].append(a)
        return ans[rowIndex]
    
    def getRow2(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            ans.append([])
            for j in range(i + 1):
                if j == 0 or j == i:
                    ans[i].append(1)
                else:
                    a = ans[i - 1][j - 1] + ans[i - 1][j]
                    ans[i].append(a)
        return ans[rowIndex]