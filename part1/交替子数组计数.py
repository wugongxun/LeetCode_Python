from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        res = cnt = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            res += cnt
        return res


print(Solution().countAlternatingSubarrays([0, 1, 1, 1]))
