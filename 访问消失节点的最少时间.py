from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj = [[] for _ in range(n)]
        for x, y, w in edges:
            adj[x].append((y, w))
            adj[y].append((x, w))

        dis = [-1] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, d in adj[x]:
                new_dis = dx + d
                if new_dis < disappear[y] and (dis[y] < 0 or new_dis < dis[y]):
                    dis[y] = new_dis
                    heappush(h, (new_dis, y))
        return dis


print(Solution().minimumTime(5, [[2, 3, 2], [4, 4, 9], [4, 0, 10], [4, 3, 4], [4, 0, 3]], [8, 20, 10, 17, 19]))
