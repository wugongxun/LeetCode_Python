from collections import Counter
from math import gcd


class Solution:
    def minAnagramLength(self, s: str) -> int:
        # for k in range(1, len(s) // 2 + 1):
        #     if len(s) % k:
        #         continue
        #     t = sorted(s[:k])
        #     if all(sorted(s[i:i + k]) == t for i in range(k, len(s), k)):
        #         return k
        # return len(s)

        n = len(s)
        g = gcd(*Counter(s).values())
        for times in range(g, 1, -1):
            if g % times:
                continue
            k = n // times
            t = sorted(s[:k])
            if all(sorted(s[i:i + k]) == t for i in range(k, n, k)):
                return k
        return n

print(Solution().minAnagramLength("jjj"))
