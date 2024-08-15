from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        pairs = list(counter.most_common())
        answer = 0
        last_f = pairs[0][1]
        for pair in pairs[1:]:
            pair = list(pair)
            if pair[1] >= last_f:
                if last_f == 1:
                    answer += pair[1]
                    pair[1] = 0
                    continue
                answer += (pair[1] - (last_f-1))
                pair[1] = last_f-1
            last_f = pair[1]
        return answer

s = Solution()
print(s.minDeletions("bbcebab"))