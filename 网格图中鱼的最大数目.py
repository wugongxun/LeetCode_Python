from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j: int):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            s = grid[i][j]
            grid[i][j] = 0
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                s += dfs(x, y)
            return s

        return max(max(dfs(i, j) for i in range(n)) for j in range(m))


print(Solution().findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
