class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ans = ""
        # i = len(a)-1
        # j = len(b)-1
        # t = 0
        # while i >= 0 or j >= 0:
        #     s = ((int(a[i]) if i >= 0 else 0) + (int(b[j]) if j >= 0 else 0) + t)
        #     t = s//2
        #     ans += str(s%2)
        #     i -= 1
        #     j -= 1
        # if t:
        #     ans += str(t)
        # return ans[::-1]
        return bin(int(a, 2) + int(b, 2))[2:]


sol = Solution()
print(sol.addBinary(a = "11", b = "1")) # 100
print(sol.addBinary(a = "1010", b = "1011")) # t
