from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and cur > nums[stack[-1]]:
                res[stack.pop()] = cur
            if i < n:
                stack.append(i)
        return res


print(Solution().nextGreaterElements([1, 2, 3, 2, 1]))
