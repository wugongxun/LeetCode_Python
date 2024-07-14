from cmath import inf
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        xs = SortedList()
        ys = SortedList()
        for x, y in points:
            xs.add(x + y)
            ys.add(y - x)
        res = inf
        for x, y in points:
            x, y = x + y, y - x
            xs.remove(x)
            ys.remove(y)
            res = min(res, max(xs[-1] - xs[0], ys[-1] - ys[0]))
            xs.add(x)
            ys.add(y)
        return res

# class Solution:
#     def minimumDistance(self, points: List[List[int]]) -> int:
#         n = len(points)
#         res = inf
#         for c in range(n):
#             mni, mnj, mxi, mxj = inf, inf, 0, 0
#             for i, (x, y) in enumerate(points):
#                 if i != c:
#                     mni = min(mni, x)
#                     mnj = min(mnj, y)
#                     mxi = max(mxi, x)
#                     mxj = max(mxj, y)
#             res = min(res, max(mxi - mni, mxj - mnj))
#         return res


print(Solution().minimumDistance([[3, 10], [5, 15], [10, 2], [4, 4]]))
