class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=len(set(s))
        b=len(set(t))
        c=len(set(zip(s,t)))
        return a==b==c