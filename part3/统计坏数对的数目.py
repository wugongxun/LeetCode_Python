from collections import defaultdict
from math import comb
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        res = comb(len(nums), 2)
        cnt = defaultdict(int)
        for i, num in enumerate(nums):
            res -= cnt[num - i]
            cnt[num - i] += 1
        return res


print(Solution().countBadPairs([4, 1, 3, 3]))
print(Solution().countBadPairs([1, 2, 3, 4, 5]))
