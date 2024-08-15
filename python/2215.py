from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [set(), set()]

        for num in nums1:
            if num not in nums2:
                ans[0].add(num)
        for num in nums2:
            if num not in nums1:
                ans[1].add(num)
        return ans