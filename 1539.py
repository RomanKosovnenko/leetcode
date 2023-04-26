from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l) // 2
            if arr[m] - m > k:
                r = m
            else:
                l = m + 1
        return l + k
