import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        for i, x in enumerate(nums):
            l = bisect.bisect_left(nums, lower - x, 0, i)
            r = bisect.bisect_right(nums, upper - x, 0, i)
            res += r - l
        return res


# print(Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6))
# print(Solution().countFairPairs([1, 7, 9, 2, 5], 11, 11))
# print(Solution().countFairPairs([0, 0, 0, 0, 0, 0], 0, 0))
print(Solution().countFairPairs([7, 9, 8, 6, -1000000000, -1000000000, -1000000000, -1000000000], -14, 11))
