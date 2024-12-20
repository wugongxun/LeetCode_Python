from functools import cache
from typing import List


class Solution:
    # def specialPerm(self, nums: List[int]) -> int:
    #     @cache
    #     def dfs(mask, prev_idx: int) -> int:
    #         if mask == 0:
    #             return 1
    #         res = 0
    #         prev = nums[prev_idx]
    #         for i, x in enumerate(nums):
    #             if mask >> i & 1 and (prev % x == 0 or x % prev == 0):
    #                 res += dfs(mask ^ (1 << i), i)
    #         return res
    #
    #     n = len(nums)
    #     u = (1 << n) - 1
    #     return sum(dfs(u ^ 1 << i, i) for i in range(n)) % 1_000_000_007

    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        u = (1 << n) - 1
        dp = [[0] * n for _ in range(u)]
        dp[0] = [1] * n
        for mask in range(1, u):
            for i, prev in enumerate(nums):
                if mask >> i & 1:
                    continue
                for j, x in enumerate(nums):
                    if mask >> j & 1 and (prev % x == 0 or x % prev == 0):
                        dp[mask][i] += dp[mask ^ (1 << j)][j]
        return sum(dp[u ^ 1 << i][i] for i in range(n)) % 1_000_000_007

print(Solution().specialPerm([2, 3, 6]))
