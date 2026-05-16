from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        return all(x == row[(i + k) % len(mat[0])] for row in mat for i, x in enumerate(row))


print(Solution().areSimilar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))
