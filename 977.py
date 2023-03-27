from typing import List


class Solution:
    def sortedSquaresTrivial(self, nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_sort = [0]*n
        l = 0
        r = n-1
        i = n-1
        while i >= 0:
            num = 0
            if abs(nums[l]) > abs(nums[r]):
                num = nums[l]
                l += 1
            else:
                num = nums[r]
                r -= 1
            nums_sort[i] = num * num
            i -= 1
        return nums_sort


sol = Solution()

print(sol.sortedSquares([-4,-1,0,3,10])) #[0,1,9,16,100]
print(sol.sortedSquares([-7,-3,2,3,11])) #[4,9,9,49,121]