from itertools import pairwise
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        split_list = [s[:spaces[0]]]
        for p, q in pairwise(spaces):
            split_list.append(s[p:q])
        split_list.append(s[spaces[-1]:])
        return " ".join(split_list)


Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
