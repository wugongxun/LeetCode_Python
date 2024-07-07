from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        for d in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
            cnt = 2
            x = rMove + d[0]
            y = cMove + d[1]
            while 0 <= x < m and 0 <= y < n:
                if board[x][y] == '.':
                    break
                if board[x][y] == color:
                    if cnt >= 3:
                        return True
                    break
                x += d[0]
                y += d[1]
                cnt += 1

        return False


print(Solution().checkMove([[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                            [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."],
                            ["W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."],
                            [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]],
                           rMove=4, cMove=3, color="B"))
