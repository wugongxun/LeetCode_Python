from cmath import inf
from itertools import permutations
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        decrease = []
        increase = []

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x > 1:
                    decrease.extend([(i, j)] * (x - 1))
                if x == 0:
                    increase.append((i, j))

        res = inf
        for from_ in permutations(decrease):
            total = 0
            for (x1, y1), (x2, y2) in zip(from_, increase):
                total += abs(x1 - x2) + abs(y1 - y2)
            res = min(res, total)
        return res


print(Solution().minimumMoves([[1, 2, 2],
                               [1, 1, 0],
                               [0, 1, 1]]))
