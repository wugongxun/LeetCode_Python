import operator
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    # def minSetSize(self, arr: List[int]) -> int:
    #     cnt = sorted(Counter(arr).values(), reverse=True)
    #     n = len(arr) // 2
    #     for i, s in enumerate(accumulate(cnt)):
    #         if s >= n:
    #             return i + 1

    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        s = 0
        for i, (_, c) in enumerate(freq.most_common()):
            s += c
            if s >= len(arr) // 2:
                return i + 1



print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
# print(Solution().minSetSize([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]))
