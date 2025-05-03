from math import inf
from typing import List, Any


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def min_rot(target: int) -> float | int:
            top_cnt = bottom_cnt = 0
            for x, y in zip(tops, bottoms):
                if x != target and y != target:
                    return inf
                if x != target:
                    top_cnt += 1
                if y != target:
                    bottom_cnt += 1
            return min(top_cnt, bottom_cnt)
        res = min(min_rot(tops[0]), min_rot(bottoms[0]))
        return -1 if res == inf else res



print(Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
