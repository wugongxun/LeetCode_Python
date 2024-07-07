from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants) - 1
        leftA, leftB = capacityA, capacityB
        res = 0
        while l <= r:
            if l == r:
                if max(leftA, leftB) < plants[l]:
                    res += 1
                break
            if leftA < plants[l]:
                leftA = capacityA - plants[l]
                res += 1
            else:
                leftA -= plants[l]
            if leftB < plants[r]:
                leftB = capacityB - plants[r]
                res += 1
            else:
                leftB -= plants[r]
            l += 1
            r -= 1
        return res


# print(Solution().minimumRefill([2, 2, 3, 3], 5, 5))
print(Solution().minimumRefill([5], 10, 8))
