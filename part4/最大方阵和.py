from cmath import inf
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt, min_abs, sum_abs = 0, inf, 0
        for row in matrix:
            for x in row:
                if x < 0:
                    cnt += 1
                    x = -x
                min_abs = min(min_abs, x)
                sum_abs += x
        return sum_abs if cnt % 2 == 0 else sum_abs - 2 * min_abs


print(Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
