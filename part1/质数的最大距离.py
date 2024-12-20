from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        def isPrime(num: int) -> bool:
            if num == 1:
                return False
            i = 2
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    return False
                i += 1
            else:
                return True

        while l < len(nums):
            if isPrime(nums[l]):
                break
            l += 1
        while r >= 0 and r >= l:
            if isPrime(nums[r]):
                break
            r -= 1
        return r - l


print(Solution().maximumPrimeDifference([4, 2, 9, 5, 3]))
