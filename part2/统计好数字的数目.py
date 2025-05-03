class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007
        return pow(5, (n - (n // 2)), MOD) * pow(4, (n // 2), MOD) % MOD

print(Solution().countGoodNumbers(1))
print(Solution().countGoodNumbers(4))
print(Solution().countGoodNumbers(806166225460393))

