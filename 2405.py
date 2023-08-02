class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = 0
        r = 1
        sub = s[0]
        while r < len(s):
            if s[r] in sub:
                ans += 1
                sub = s[r]
            else:
                sub += s[r]
            r+=1
        if sub:
            ans+=1
        return ans
