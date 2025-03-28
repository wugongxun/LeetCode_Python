from functools import cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def weight(x: int) -> int:
            if x == 1:
                return 0
            if x % 2:
                return weight(3 * x + 1) + 1
            else:
                return weight(x // 2) + 1

        weight = [weight(i) for i in range(lo, hi + 1)]
        ids = [i for i, _ in enumerate(range(lo, hi + 1))]
        ids.sort(key=lambda x: weight[x])
        return ids[k - 1] + lo

print(Solution().getKth(7, 11, 4))