class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.strip()
        l = st.split()
        return " ".join(reversed(l))
