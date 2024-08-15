class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        first = 0
        second = 1
        for _ in range(2, n+1):
            second, first = first+second, second
        return second

    def fibdp(self, n: int) -> int:
        if n < 2:
            return n
        answer = [0]*(n+1)
        answer[1] = 1

        for i in range(2, n+1):
            answer[i] = answer[i-2] + answer[i-1]
        return answer[n]
