from cmath import inf
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        mx, mn, pre_mx = 0, inf, 0
        for i, num in enumerate(nums):
            if i == 0 or num.bit_count() == nums[i - 1].bit_count():
                mx = max(mx, num)
                mn = min(mn, num)
            else:
                if mn < pre_mx:
                    return False
                pre_mx = mx
                mx, mn = num, num
        return mn >= pre_mx


print(Solution().canSortArray([3, 16, 8, 4, 2]))
