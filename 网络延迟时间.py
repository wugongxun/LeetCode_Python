from cmath import inf
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] * n for _ in range(n)]
        for x, y, d in times:
            adj[x - 1].append((y - 1, d))
        dis = [inf] * n
        dis[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, d in adj[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    heappush(h, (new_dis, y))
        mx = max(dis)
        return mx if mx < inf else -1

    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    #     adj = [[inf] * n for _ in range(n)]
    #     for x, y, d in range(times):
    #         adj[x - 1][y - 1] = d
    #     dis = [inf] * n
    #     res = dis[k - 1] = 0
    #     done = [False] * n
    #     while True:
    #         x = -1
    #         for i, ok in enumerate(done):
    #             if not ok and (x < 0 or dis[i] < dis[x]):
    #                 x = i
    #         if x < 0:
    #             return res
    #         if dis[x] == inf:
    #             return -1
    #         res = dis[x]
    #         done[x] = True
    #         for y, d in enumerate(adj[x]):
    #             dis[y] = min(dis[y], dis[x] + d)