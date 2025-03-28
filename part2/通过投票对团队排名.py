from collections import defaultdict
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        cnts = defaultdict(lambda: [0] * n)
        for vote in votes:
            for i, ch in enumerate(vote):
                cnts[ch][i] -= 1
        return "".join(sorted(cnts, key=lambda x: (cnts[x], x)))


# print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
print(Solution().rankTeams(["WXYZ", "XYZW"]))
