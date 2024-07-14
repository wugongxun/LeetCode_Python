from cmath import inf
from functools import cache
from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        @cache
        def dfs(l1, l2, r1, r2: int) -> int:
            res = inf
            for i in range(l1 + 1, l2):
                res = min(res, dfs(l1, i, r1, r2) + dfs(i, l2, r1, r2) + horizontalCut[i - 1])
            for j in range(r1 + 1, r2):
                res = min(res, dfs(l1, l2, r1, j) + dfs(l1, l2, j, r2) + verticalCut[j - 1])
            return 0 if res == inf else res

        return dfs(0, m, 0, n)


print(Solution().minimumCost(3, 2, [1, 3], [5]))
