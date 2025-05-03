from collections import defaultdict
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        cnt = defaultdict(int)
        res = left = 0
        for x in nums:
            cnt[x] += 1
            while len(cnt) == k:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            res += left
        return res


print(Solution().countCompleteSubarrays([1, 3, 1, 2, 2]))
