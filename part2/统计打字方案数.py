from itertools import groupby

MOD = 1_000_000_007
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]

for _ in range(10 ** 5 - 3):
    f.append((f[-1] + f[-2] + f[-3]) % MOD)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        res = 1
        for ch, s in groupby(pressedKeys):
            m = len(list(s))
            res = res * (g[m] if ch == "7" or ch == "9" else f[m]) % MOD
        return res


print(Solution().countTexts("22233222"))
