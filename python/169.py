from collections import Counter
from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         a = Counter(nums).most_common(1)[0]
#         return a[0]

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[int((len(nums)-1)/2)]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))