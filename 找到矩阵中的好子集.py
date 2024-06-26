from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        mask_to_idx = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, x in enumerate(row):
                mask |= x << j
            if mask == 0:
                return [i]
            mask_to_idx[mask] = i
        for k1, v1 in mask_to_idx.items():
            for k2, v2 in mask_to_idx.items():
                if k1 & k2 == 0:
                    return [min(v1, v2), max(v1, v2)]
        return []


print(Solution().goodSubsetofBinaryMatrix([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1]]))
