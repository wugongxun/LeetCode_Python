from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        free = [startTime[0]] + [s - e for s, e in zip(startTime[1:], endTime)] + [eventTime - endTime[n - 1]]
        res = s = 0
        for i, f in enumerate(free):
            s += f
            if i < k:
                continue
            res = max(res, s)
            s -= free[i - k]
        return res
