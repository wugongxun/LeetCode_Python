from cmath import inf
from itertools import accumulate
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos = []
        c = 0
        for i, num in enumerate(nums):
            if num == 0:
                continue
            pos.append(i)
            c = max(c, 1)
            if i > 0 and nums[i - 1]:
                if i > 1 and nums[i - 2]:
                    c = 3
                else:
                    c = max(c, 2)
        c = min(c, k)
        if maxChanges >= k - c:
            return max(0, c - 1) + (k - c) * 2

        n = len(pos)
        prefix = list(accumulate(pos, initial=0))

        res = inf
        size = k - maxChanges
        for r in range(size, n + 1):
            l = r - size
            mid = (l + r) // 2
            s1 = pos[mid] * (mid - l) - (prefix[mid] - prefix[l])
            s2 = prefix[r] - prefix[mid] - pos[mid] * (r - mid)
            res = min(res, s1 + s2)
        return res + maxChanges * 2


print(Solution().minimumMoves([1, 0, 1, 0, 1], 3, 0))
