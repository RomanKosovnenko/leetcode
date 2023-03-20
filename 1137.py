class Solution:
    def tribonacciConstantMemory(self, n: int) -> int:
        T = [0]*38
        T[1] = T[2] = 1
        for i in range(3, 38):
            T[i] = T[i-2]+T[i-1]+T[i-3]
        return T[n]

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        T = [0]*(n+1)
        T[1] = T[2] = 1
        for i in range(3, n+1):
            T[i] = T[i-2]+T[i-1]+T[i-3]
        return T[n]
