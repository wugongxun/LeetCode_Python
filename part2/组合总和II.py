from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        path = []
        candidates.sort()

        def dfs(i: int, r: int):
            if r == 0:
                res.append(path[:])
                return
            for j in range(i, n):
                if r < candidates[j]:
                    break
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j + 1, r - candidates[j])
                path.pop()

        dfs(0, target)
        return res


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
