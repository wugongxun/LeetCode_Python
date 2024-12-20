from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        res = ListNode(-1, head)
        cur = res
        while cur.next.val in s:
            if cur.next.val in nums:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return res.next


print(Solution().modifiedList([1, 7, 6, 2, 4], ListNode(3, ListNode(7, ListNode(1, ListNode(8, ListNode(1)))))))
