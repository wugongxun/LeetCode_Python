from functools import cache


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        pow3 = [3 ** i for i in range(m)]
        valid = []
        for color in range(3 ** m):
            for i in range(1, m):
                if color // pow3[i] % 3 == color // pow3[i - 1] % 3:
                    break
            else:
                valid.append(color)
        nv = len(valid)
        nxt = [[] for _ in range(nv)]
        for i, c1 in enumerate(valid):
            for j, c2 in enumerate(valid):
                for p in pow3:
                    if c1 // p % 3 == c2 // p % 3:
                        break
                else:
                    nxt[i].append(j)
        MOD = 1_000_000_007

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return 1
            return sum(dfs(i - 1, k) for k in nxt[j]) % MOD

        return sum(dfs(n - 1, j) for j in range(nv)) % MOD


print(Solution().colorTheGrid(5, 5))
