class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = {}
        for i in range(len(arr)):
            if 2*arr[i] in h:
                return True
            if arr[i] % 2 == 0 and arr[i]/2 in h:
                return True
            h[arr[i]] = 1
        return False
