from typing import List
from heapq import heappop, heapreplace, heapify


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapify(nums)
        while True:
            x = heappop(nums)
            if x >= k:
                return res
            heapreplace(nums, min(x, nums[0]) * 2 + max(x, nums[0]))
            res += 1



print(Solution().minOperations([2, 11, 10, 1, 3], 10))
