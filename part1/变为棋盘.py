from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        first_row = board[0]
        row_cnt = Counter(first_row)
        if abs(row_cnt[0] - row_cnt[1]) > 1:
            return -1

        first_col = list(next(zip(*board)))
        col_cnt = Counter(first_col)
        if abs(col_cnt[0] - col_cnt[1]) > 1:
            return -1

        for row in board:
            same = row[0] == first_row[0]
            for x, y in zip(row, first_row):
                if (x == y) != same:
                    return -1

        def min_swap(arr: List[int], cnt: Counter) -> int:
            n = len(arr)
            x0 = 1 if cnt[1] > cnt[0] else 0
            diff = sum(i % 2 ^ x ^ x0 for i, x in enumerate(arr))
            return diff // 2 if n % 2 else min(diff, n - diff) // 2

        return min_swap(first_row, row_cnt) + min_swap(first_col, col_cnt)


print(Solution().movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]))
print(Solution().movesToChessboard([[1, 0], [1, 0]]))
