from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_has = [[False] * 9 for _ in range(9)]
        col_has = [[False] * 9 for _ in range(9)]
        box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        empty_pos = []

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == ".":
                    empty_pos.append((i, j))
                else:
                    x = int(b) - 1
                    row_has[i][x] = True
                    col_has[j][x] = True
                    box_has[i // 3][j // 3][x] = True

        def dfs(k: int) -> bool:
            if k >= len(empty_pos):
                return True
            i, j = empty_pos[k]
            for x in range(9):
                if row_has[i][x] or col_has[j][x] or box_has[i // 3][j // 3][x]:
                    continue
                row_has[i][x] = True
                col_has[j][x] = True
                box_has[i // 3][j // 3][x] = True
                board[i][j] = str(x + 1)
                if dfs(k + 1):
                    return True
                row_has[i][x] = False
                col_has[j][x] = False
                box_has[i // 3][j // 3][x] = False

            return False

        dfs(0)