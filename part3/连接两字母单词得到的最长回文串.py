from collections import defaultdict, Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = odd = 0
        for w, c in cnt.items():
            if w[0] == w[1]:
                res += c - c % 2
                odd |= c % 2
            elif w[0] < w[1]:
                res += min(c, cnt[w[::-1]]) * 2
        return (res + odd) * 2


# print(Solution().longestPalindrome(["lc", "cl", "gg"]))
print(
    Solution().longestPalindrome(["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]))
