from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] ^ (1 << (ord(s[i]) - ord('a')))
        res = []
        for l, r, k in queries:
            cnt = (pre[l] ^ pre[r + 1]).bit_count()
            res.append(cnt <= k * 2 + 1)
        return res


print(Solution().canMakePaliQueries("abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))
