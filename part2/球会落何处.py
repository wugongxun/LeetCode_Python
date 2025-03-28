from functools import cache
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        res = [-1] * n
        for j in range(n):
            cur_col = j
            for row in grid:
                d = row[cur_col]
                cur_col += d
                if cur_col < 0 or cur_col >= n or row[cur_col] != d:
                    break
            else:
                res[j] = cur_col
        return res

    # def findBall(self, grid: List[List[int]]) -> List[int]:
    #     m, n = len(grid), len(grid[0])
    #     @cache
    #     def dfs(i, j: int):
    #         if i >= m:
    #             return j
    #         if (grid[i][j] == 1 and j == n - 1) or (grid[i][j] == 1 and grid[i][j + 1] == -1) or (grid[i][j] == -1 and j == 0) or (grid[i][j] == -1 and grid[i][j - 1] == 1):
    #             return -1
    #         return dfs(i + 1, j + 1) if grid[i][j] == 1 else dfs(i + 1, j - 1)
    #
    #     return [dfs(0, j) for j in range(n)]


print(Solution().findBall(
    [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
