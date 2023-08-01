from collections import Counter
from typing import List

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = {}
#         columns = {}
#         nines = {}
#
#         for i in range(9):
#             rows[i] = set()
#             columns[i] = set()
#
#         for i in range(3):
#             for j in range(3):
#                 nines[(i, j)] = set()
#
#         for i in range(9):
#             for j in range(9):
#                 cell = board[i][j]
#                 if cell == ".":
#                     continue
#                 if cell in rows[i] or cell in columns[j] or cell in nines[i//3, j//3]:
#                     return False
#                 rows[i].add(cell)
#                 columns[j].add(cell)
#                 nines[i//3, j//3].add(cell)
#         return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def validate_row(i):
#             hist = Counter(board[i])
#             hist.pop(".")
#             return all(ctn == 1 for ctn in hist.values())

#         def validate_column(i):
#             column = [board[j][i] for j in range(len(board))]
#             hist = Counter(column)
#             hist.pop(".")
#             return all(ctn == 1 for ctn in hist.values())

#         def validate_nine(s_r, s_c):
#             nine = []
#             for i in range(s_r, s_r+3):
#                 for j in range(s_c, s_c+3):
#                     nine.append(board[i][j])
#             hist = Counter(nine)
#             hist.pop(".")
#             return all(ctn == 1 for ctn in hist.values())

#         for i in range(len(board)):
#             if not validate_row(i):
#                 return False

#         for i in range(len(board[0])):
#             if not validate_column(i):
#                 return False

#         for i in [0,3,6]:
#             for j in [0,3,6]:
#                 if not validate_nine(i, j):
#                     return False
#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate_row(i):
            c = Counter(board[i])
            c.pop(".")
            for val in c.values():
                if val > 1:
                    return False
            return True

        def validate_column(i):
            column = [row[i] for row in board]
            c = Counter(column)
            c.pop(".")
            for val in c.values():
                if val > 1:
                    return False
            return True

        def validate_nine(r, c):
            l = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    l.append(board[i][j])
            c = Counter(l)
            c.pop(".")
            for val in c.values():
                if val > 1:
                    return False
            return True

        for row in range(len(board)):
            if not validate_row(row):
                return False
        for column in range(len(board[0])):
            if not validate_column(column):
                return False
        for row in [0,3,6]:
            for column in [0,3,6]:
                if not validate_nine(row, column):
                    return False
        return True

sol = Solution()
print(sol.isValidSudoku(
    [
    [".",".","4", ".",".",".", "6","3","."],
    [".",".",".", ".",".",".", ".",".","."],
    ["5",".",".", ".",".",".", ".","9","."],

    [".",".",".", "5","6",".", ".",".","."],
    ["4",".","3", ".",".",".", ".",".","1"],
    [".",".",".", "7",".",".", ".",".","."],
    
    [".",".",".", "5",".",".", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."]])) # f

print(sol.isValidSudoku([
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])) # t
print(sol.isValidSudoku(
    [
    [".",".",".", "1",".","8", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."],
    [".",".",".", ".",".",".", ".",".","."],

    ["4",".",".", ".",".","7", ".",".","."],
    [".",".",".", "7",".",".", "8","4","1"],
    [".",".",".", ".","7",".", ".",".","."],

    [".",".",".", ".",".",".", "6",".","."],
    [".",".",".", "6",".",".", ".",".","."],
    ["6",".",".", ".",".",".", ".",".","."]
    ])) # f

