from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        columns = len(image[0])

        def change_color(sr, sc, color, base_color):
            if not (0 <= sr < rows and 0 <= sc < columns and image[sr][sc] == base_color):
                return
            image[sr][sc] = color
            change_color(sr, sc -1, color, base_color)
            change_color(sr, sc +1, color, base_color)
            change_color(sr-1, sc, color, base_color)
            change_color(sr+1, sc, color, base_color)
        
        change_color(sr, sc, color, image[sr][sc])
        return image




sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)) # t
print(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 0)) # t
# print(sol.checkInclusion("ab", "eidboaoo")) # f