class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = []
        len1 = len(word1)
        len2 = len(word2)
        lenm = min(len1, len2)

        while i < lenm:
            res.append(word1[i]+word2[i])
            i += 1

        if i < len1:
            res.append(word1[i:])

        if i < len2:
            res.append(word2[i:])
        return "".join(res)