from cmath import inf
from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        adj = [[inf] * n for _ in range(n)]
        for (u, v, w) in roads:
            adj[u][v] = min(adj[u][v], w)
            adj[v][u] = min(adj[v][u], w)
        f = [None] * n

        def check(s: int) -> int:
            for i, row in enumerate(adj):
                f[i] = row.copy()

            for k in range(n):
                if (s >> k & 1) == 0:
                    continue
                for i in range(n):
                    if (s >> k & 1) == 0 or f[i][k] == inf:
                        continue
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            for i, di in enumerate(f):
                if (s >> i & 1) == 0:
                    continue
                for j, dj in enumerate(di[:i]):
                    if s >> j & 1 and dj > maxDistance:
                        return 0
            return 1

        return sum(check(s) for s in range(1 << n))


print(Solution().numberOfSets(3, 5, [[0, 1, 2], [1, 2, 10], [0, 2, 10]]))
