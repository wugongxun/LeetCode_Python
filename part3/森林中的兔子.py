from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        for k, v in Counter(answers).items():
            res += (v + k) // (k + 1) * (k + 1)
        return res

print(Solution().numRabbits([1, 1, 2]))
