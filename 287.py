from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numbers = [0]*(10**5+1)

        for num in nums:
            if numbers[num] == 0:
                numbers[num] += 1
            else:
                return num
        return 0
