from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        prefixSum = defaultdict(int)
        n = len(wall)
        for i in range(0, n):
            curSum = 0
            for j in range(0, len(wall[i]) - 1):
                curSum += wall[i][j]
                prefixSum[curSum] += 1
        return n - max(prefixSum.values(), default=0)


print(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
