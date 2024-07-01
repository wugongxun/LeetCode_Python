from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        target += sum(nums)
        if target < 0 or target % 2 != 0:
            return 0
        target //= 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for s in range(target, num - 1, - 1):
                dp[s] = dp[s] + dp[s - num]
        return dp[target]

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     target += sum(nums)
    #     if target < 0 or target % 2 != 0:
    #         return 0
    #     target //= 2
    #     dp = [[0] * (target + 1) for _ in range(n + 1)]
    #     dp[0][0] = 1
    #     for i, num in enumerate(nums):
    #         for s in range(target + 1):
    #             if s < num:
    #                 dp[i + 1][s] = dp[i][s]
    #             else:
    #                 dp[i + 1][s] = dp[i][s] + dp[i][s - num]
    #     return dp[n][target]

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     target += sum(nums)
    #     if target < 0 or target % 2 != 0:
    #         return 0
    #     target //= 2
    #
    #     @cache
    #     def dfs(i, s: int) -> int:
    #         if i < 0:
    #             return 1 if s == 0 else 0
    #         if s < nums[i]:
    #             return dfs(i - 1, s)
    #         return dfs(i - 1, s) + dfs(i - 1, s - nums[i])
    #
    #     return dfs(n - 1, target)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
