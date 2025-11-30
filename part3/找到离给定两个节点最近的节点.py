from cmath import inf
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        res = -1
        min_dis = inf

        def calc_dis(x: int) -> List[int]:
            dis = [inf] * n
            d = 0
            while x != -1 and dis[x] == inf:
                dis[x] = d
                d += 1
                x = edges[x]
            return dis

        d1 = calc_dis(node1)
        d2 = calc_dis(node2)

        for i in range(n):
            d = max(d1[i], d2[i])
            if d < min_dis:
                min_dis = d
                res = i

        return res


# print(Solution().closestMeetingNode([2, 2, 3, -1], 0, 1))
print(Solution().closestMeetingNode([4, 3, 0, 5, 3, -1], 4, 0))
