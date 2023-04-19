from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = len(arr1)
        l2 = len(arr2)
        for num in arr1:
            l, r = 0, l2-1
            while l<=r:
                m = (l+r)//2
                if abs(num-arr2[m]) <= d:
                    res -= 1
                    break
                if arr2[m] > num:
                    r = m-1
                else:
                    l = m+1
        return res



solution = Solution()
print(solution.findTheDistanceValue([4,-3,-7,0,-10], [10], 69)) # 1
print(solution.findTheDistanceValue([4,5,8], [10,9,1,8], 2)) # 2
print(solution.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3)) # 2
print(solution.findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6)) # 1