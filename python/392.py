class Solution:
    def isSubsequenceDP(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m] == n

    def isSubsequenceTwoPointers(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j +=1
        return i == n

    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        for char in t:
            if i == n: return True
            if s[i] == char:
                i += 1
        return i == n
