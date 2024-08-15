class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val == 1 and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                            if 0 <= nr < row_len and 0 <= nc < col_len and \
                                    grid[nr][nc] == 1 and (nr, nc) not in seen:
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans