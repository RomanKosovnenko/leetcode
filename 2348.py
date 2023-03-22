class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        answer = 0
        for num in nums:
            if num:
                count = 0
            else:
                count += 1
            answer += count
        return answer