from cmath import inf
from functools import cache
from typing import List


class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[inf] * n for _ in range(n)]
        for (f, t, w) in edges:
            adj[f][t] = adj[t][f] = w

        dp = adj
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        res = 0
        min_cnt = inf
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and dp[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= min_cnt:
                min_cnt = cnt
                res = i
        return res


    # def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    #     adj = [[inf] * n for _ in range(n)]
    #     for (f, t, w) in edges:
    #         adj[f][t] = adj[t][f] = w
    #     dp = [[[0] * n for _ in range(n)] for _ in range(n + 1)]
    #     dp[0] = adj
    #     for k in range(n):
    #         for i in range(n):
    #             for j in range(n):
    #                 dp[k + 1][i][j] = min(dp[k][i][j], dp[k][i][k] + dp[k][k][j])
    #     res = 0
    #     min_cnt = inf
    #     for i in range(n):
    #         cnt = 0
    #         for j in range(n):
    #             if i != j and dp[n][i][j] <= distanceThreshold:
    #                 cnt += 1
    #         if cnt <= min_cnt:
    #             min_cnt = cnt
    #             res = i
    #     return res

    # def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    #     adj = [[inf] * n for _ in range(n)]
    #     for (f, t, w) in edges:
    #         adj[f][t] = adj[t][f] = w
    #
    #     @cache
    #     def dfs(k, i, j: int) -> int:
    #         if k < 0:
    #             return adj[i][j]
    #         return min(dfs(k - 1, i, j), dfs(k - 1, i, k) + dfs(k - 1, k, j))
    #
    #     res = 0
    #     min_cnt = inf
    #     for i in range(n):
    #         cnt = 0
    #         for j in range(n):
    #             if j != i and dfs(n - 1, i, j) <= distanceThreshold:
    #                 cnt += 1
    #         if cnt <= min_cnt:
    #             min_cnt = cnt
    #             res = i
    #     return res
