from itertools import accumulate
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = list(accumulate(nums, initial=0))
        s = prefix[-1] % p
        if s == 0:
            return 0
        res = n = len(nums)
        last: dict[int, int] = {}
        for i, x in enumerate(prefix):
            last[x % p] = i
            j = last.get((x - s + p) % p)
            if j is not None:
                res = min(res, i - j)
        return res if res < n else -1


print(Solution().minSubarray([8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], 148))
