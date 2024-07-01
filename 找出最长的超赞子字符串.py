class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        pos = [n] * (1 << 10)
        pos[0] = -1
        res = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            res = max(res, i - pos[pre], max(i - pos[pre ^ (1 << d)] for d in range(n)))
            if pos[pre] == n:
                pos[pre] = i
        return res


print(Solution().longestAwesome('3242415'))
