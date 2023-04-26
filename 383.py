class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        while i < len(ransomNote) and ransomNote != "":
            if ransomNote[i] in magazine:
                Index = magazine.index(ransomNote[i])
                ransomNote = ransomNote[:i] + ransomNote[i + 1:]
                magazine = magazine[:Index] + magazine[Index + 1:]
            else:
                return False
        return True