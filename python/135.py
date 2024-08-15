from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n-1):
            if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                candies[i] = candies[i-1] + 1
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i + 1] + 1
        print(candies)
        return sum(candies)

s = Solution()
print(s.candy([29,51,87,87,72,12])) #12