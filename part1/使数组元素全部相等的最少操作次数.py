from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        prefix = list(accumulate(nums, initial=0))
        res = []
        for q in queries:
            index = bisect_left(nums, q)
            s1 = q * index - prefix[index]
            s2 = prefix[n] - prefix[index] - q * (n - index)
            res.append(s1 + s2)
        return res


print(Solution().minOperations(
    [47, 50, 97, 58, 87, 72, 41, 63, 41, 51, 17, 21, 7, 100, 69, 66, 79, 92, 84, 9, 57, 26, 26, 28, 83, 38],
    [50, 84, 76, 41, 64, 82, 20, 22, 64, 7, 38, 92, 39, 28, 22, 3, 41, 46, 47, 50, 88, 51, 9, 49, 38, 67, 26, 65, 89,
     27, 71, 25, 77, 72, 65, 41, 84, 68, 51, 26, 84, 24, 79, 41, 96, 83, 92, 9, 93, 84, 35, 70, 74, 79, 37, 38, 26, 26,
     41, 26]))
