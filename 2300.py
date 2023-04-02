import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        #spells.sort()
        potions.sort()
        pairs = []
        pot_len = len(potions)
        maxPotion = potions[pot_len - 1]
        for spell in spells:
            minPotion = (success + spell - 1) // spell
            if minPotion > maxPotion:
                pairs.append(0)
                continue
            index = bisect.bisect_left(potions, minPotion)
            pairs.append(pot_len - index)
        return pairs

sol = Solution()
print(sol.successfulPairs([5,1,3], [1,2,3,4,5], 7)) # [4,0,3]
print(sol.successfulPairs([3,1,2], [8,5,8], 16)) # [2,0,2]