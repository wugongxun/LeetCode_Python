from functools import cache
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f = [0] * n
        from_ = [-1] * n
        max_i = 0
        for i, x in enumerate(nums):
            for j in range(i):
                if x % nums[j] == 0 and f[j] > f[i]:
                    f[i] = f[j]
                    from_[i] = j
            f[i] += 1
            if f[i] > f[max_i]:
                max_i = i

        path = []
        i = max_i
        while i >= 0:
            path.append(nums[i])
            i = from_[i]
        return path


        # nums.sort()
        # n = len(nums)
        # from_ = [-1] * n
        #
        # @cache
        # def dfs(i: int) -> int:
        #     res = 0
        #     for j in range(i):
        #         if nums[i] % nums[j]:
        #             continue
        #         f = dfs(j)
        #         if f > res:
        #             res = f
        #             from_[i] = j
        #     return res + 1
        #
        # max_f = max_i = 0
        # for i in range(n):
        #     f = dfs(i)
        #     if f > max_f:
        #         max_f = f
        #         max_i = i
        #
        # path = []
        # i = max_i
        # while i >= 0:
        #     path.append(nums[i])
        #     i = from_[i]
        # return path


print(Solution().largestDivisibleSubset([1, 2, 3]))
