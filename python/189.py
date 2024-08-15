from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[::] = nums[n-k:] + nums[:n-k]


solution = Solution()
print(solution.rotate([1,2,3,4,5,6,7], 3))
print(solution.rotate([1,2], 5))