from cmath import inf
from collections import Counter
from functools import cache


class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        # @cache
        # def dfs(i: int) -> int:
        #     if i >= len(s):
        #         return 0
        #     cnt = Counter()
        #     res = inf
        #     max_cnt = 0
        #     for j, c in enumerate(s[i:]):
        #         cnt[c] += 1
        #         max_cnt = max(max_cnt, cnt[c])
        #         if j + 1 == len(cnt) * max_cnt:
        #             res = min(res, dfs(i + j + 1) + 1)
        #     return res
        # return dfs(0)

        n = len(s)
        dp = [inf] * n + [0]
        for i in range(n - 1, -1, -1):
            cnt = Counter()
            max_cnt = 0
            for j, c in enumerate(s[i:]):
                cnt[c] += 1
                max_cnt = max(max_cnt, cnt[c])
                if j + 1 == len(cnt) * max_cnt:
                    dp[i] = min(dp[i], dp[i + j + 1] + 1)
        return dp[0]

print(Solution().minimumSubstringsInPartition("fabccddg"))