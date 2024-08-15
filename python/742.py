from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums[1:])
        if l_sum == r_sum:
            return 0
        for i in range(1, len(nums)):
            l_sum = l_sum + nums[i-1]
            r_sum = r_sum - nums[i]
            if l_sum == r_sum:
                return i
        return -1
    
sol = Solution()

print(sol.pivotIndex([1,7,3,6,5,6])) #3
print(sol.pivotIndex([1,2,3])) #-1
print(sol.pivotIndex([2,1,-1])) #0
print(sol.pivotIndex([1,-1,2])) #2