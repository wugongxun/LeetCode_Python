from cmath import inf
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, mn, mx = 0, inf, -inf
        for arr in arrays:
            res = max(res, mx - arr[0], arr[-1] - mn)
            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])
        return res


# print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
print(Solution().maxDistance([[1], [1]]))
