from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        res = 0
        visited = [False] * n
        visited[0] = True

        def dfs(cur, sumTime, sumValue: int):
            if cur == 0:
                nonlocal res
                res = max(res, sumValue)
            for nex, t in adj[cur]:
                if t + sumTime > maxTime:
                    continue
                if visited[nex]:
                    dfs(nex, sumTime + t, sumValue)
                else:
                    visited[nex] = True
                    dfs(nex, sumTime + t, sumValue + values[nex])
                    visited[nex] = False

        dfs(0, 0, values[0])
        return res


print(Solution().maximalPathQuality([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49))
