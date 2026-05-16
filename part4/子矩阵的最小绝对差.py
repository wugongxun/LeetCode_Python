from cmath import inf
from itertools import pairwise
from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                a = []
                for row in grid[i: i + k]:
                    a += row[j: j + k]
                a.sort()
                r = inf
                for x, y in pairwise(a):
                    if x != y:
                        r = min(r, abs(x - y))
                if r != inf:
                    res[i][j] = r
        return res


print(Solution().minAbsDiff([[1, -2, 3], [2, 3, 5]], 2))
