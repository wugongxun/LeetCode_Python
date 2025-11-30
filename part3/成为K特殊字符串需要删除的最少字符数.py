from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        vals = sorted(Counter(word).values())
        max_save = 0
        for i, base in enumerate(vals):
            max_save = max(max_save, sum(min(c, base + k) for c in vals[i:]))
        return len(word) - max_save


print(Solution().minimumDeletions("aabcaba", 0))
