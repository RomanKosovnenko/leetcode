from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answers = [0] * len(triangle)
        answers[0]=0
        for i in range(1, len(triangle)):
            if triangle[i][answers[i-1]] > triangle[i][answers[i-1]+1]:
                answers[i] = answers[i-1]+1
            else:
                answers[i] = answers[i-1]
        return sum(triangle[idx][i] for idx, i in enumerate(answers))
