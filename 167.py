from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = len(numbers)
        j = n-1

        while i<j:
            s = numbers[i]+numbers[j]
            if s == target:
                return [i+1, j+1]
            if s > target:
                j -= 1
            else:
                i += 1