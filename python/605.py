class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 1
        flowerbed = [0] + flowerbed + [0]
        l = len(flowerbed)
        
        while i < l-1 and n > 0:
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            i += 1
        
        if n > 0:
            return False
        else: 
            return True
