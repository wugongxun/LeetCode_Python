from itertools import product
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = map(max, grid)
        col_max = map(max, zip(*grid))
        return sum(map(min, product(row_max, col_max))) - sum(map(sum, grid))

    # def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     row_max, col_max = [0] * n, [0] * n
    #     for i, row in enumerate(grid):
    #         row_max[i] = max(row)
    #         for j, x in enumerate(row):
    #             col_max[j] = max(col_max[j], x)
    #     res = 0
    #     for i, row in enumerate(grid):
    #         for j, x in enumerate(row):
    #             res += min(row_max[i], col_max[j]) - x
    #     return res


print(Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
