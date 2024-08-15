from typing import List
from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect_right(letters, target)
        return letters[0] if idx == len(letters) else letters[idx]


sol = Solution()

print(sol.nextGreatestLetter(["x","x","y","y"], "z")) #x
print(sol.nextGreatestLetter(["c","f","j"], "d")) #f
print(sol.nextGreatestLetter(["c","f","j"], "c"))#f
print(sol.nextGreatestLetter(["c","f","j"], "a")) #c