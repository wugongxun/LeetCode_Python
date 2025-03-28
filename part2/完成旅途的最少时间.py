from bisect import bisect_left
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_t = min(time)
        avg = (totalTrips - 1) // len(time) + 1
        l, r = min_t * avg, min(max(time) * avg, min_t * totalTrips)
        return bisect_left(range(r), totalTrips, l, key=lambda x: sum(x // i for i in time))


# print(minimumTime([1, 2, 3], 5))
print(Solution().minimumTime([5, 10, 10], 9))
