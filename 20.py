class Solution:
    def isValid(self, s: str) -> bool:
        ss_ = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stk = []
        for el in s:
            if el in ss_ and len(stk) and stk[-1] == ss_[el]:
                stk.pop()
            else:
                stk.append(el)

        if len(stk) > 0:
            return False
        return True