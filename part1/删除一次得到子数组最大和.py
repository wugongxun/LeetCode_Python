from cmath import inf
from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        res = dp0 = dp1 = -inf
        for x in arr:
            dp1 = max(dp1 + x, dp0)
            dp0 = max(dp0, 0) + x
            res = max(res, dp0, dp1)
        return res

    # def maximumSum(self, arr: List[int]) -> int:
    #     @cache
    #     def dfs(i, j: int) -> int:
    #         if i < 0:
    #             return -inf
    #         if j == 0:
    #             return max(dfs(i - 1, 0), 0) + arr[i]
    #         return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))
    #
    #     return max(max(dfs(i, 0), dfs(i, 1)) for i in range(len(arr)))


print(Solution().maximumSum([1, -2, -2, 3]))
