from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ids = sorted(range(len(nums)), key=lambda x: nums[x], reverse=True)
        return [nums[i] for i in sorted(ids[:k])]
