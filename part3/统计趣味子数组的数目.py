from itertools import accumulate
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        pre_sum = list(accumulate((x % modulo == k for x in nums), initial=0))
        cnt = [0] * min(len(nums) + 1, modulo)
        res = 0
        for x in pre_sum:
            if x >= k:
                res += cnt[(x - k) % modulo]
            cnt[x % modulo] += 1
        return res


print(Solution().countInterestingSubarrays([3, 2, 4], 2, 1))
