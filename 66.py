from typing import List


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         temp = 1
#         for i in range(len(digits)-1, -1, -1):
#             digits[i], temp = (digits[i]+temp)%10, (digits[i]+temp)//10
#             if temp == 0:
#                 return digits
#         if temp != 0:
#             digits.insert(0, temp)
#         return digits

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits

solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))
