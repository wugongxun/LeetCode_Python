from functools import cache

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * (k + 1) for _ in range(n + 4)] for _ in range(n + 4)]
        for i in range(2, n + 2):
            for j in range(2, n + 2):
                dp[i][j][0] = 1
        for step in range(1, k + 1):
            for i in range(2, n + 2):
                for j in range(2, n + 2):
                    dp[i][j][step] = sum(dp[i + x][j + y][step - 1] for x, y in [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]) / 8
        return dp[row + 2][column + 2][k]



    # def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    #     @cache
    #     def dfs(i, j, step: int) -> float:
    #         if not (0 <= i < n and 0 <= j < n):
    #             return 0
    #         if step == 0:
    #             return 1
    #         return sum(dfs(i + x, j + y, step - 1) for x, y in [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]) / 8
    #     return dfs(row, column, k)

print(Solution().knightProbability(3, 2, 0, 0))
