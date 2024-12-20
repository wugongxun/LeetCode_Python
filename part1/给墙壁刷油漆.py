from cmath import inf
from functools import cache
from typing import List


class Solution:
    # def paintWalls(self, cost: List[int], time: List[int]) -> int:
    #     n = len(cost)
    #
    #     # i为第刷第i面墙
    #     # j为剩余的免费时间
    #     @cache
    #     def dfs(i, j: int) -> int:
    #         if j > i:
    #             return 0
    #         if i < 0:
    #             return inf
    #         return min(dfs(i - 1, j + time[i]) + cost[i], dfs(i - 1, j - 1))
    #
    #     return dfs(n - 1, 0)
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [inf] * n
        for t, c in zip(time, cost):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - t - 1, 0)] + c)
        return dp[n]


print(Solution().paintWalls([1, 2, 3, 2], [1, 2, 3, 2]))
