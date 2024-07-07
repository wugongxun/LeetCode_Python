from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'X' and (j == 0 or row[j - 1] != 'X') and (i == 0 or board[i - 1][j] != 'X'):
                    res += 1
        return res


print(Solution().countBattleships([['X', 'X', 'X']]))
