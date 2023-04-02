class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # type: ignore
        n = len(s)
        if n < 2:
            return n
        m = 0
        l, r = 0, 0
        substring = set(s[l:r])
        while r < n:
            if s[r] in substring:
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
            substring.add(s[r])
            m = max(m, len(substring))
            r += 1
        return m

sol = Solution()
print(sol.lengthOfLongestSubstring("au")) # 2
print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
