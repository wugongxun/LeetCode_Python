from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        vis = [False] * n
        res = []

        def dfs(i: int) -> None:
            vis[i] = True
            for email in accounts[i][1:]:
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_idx[email]:
                    if not vis[j]:
                        dfs(j)

        for i, b in enumerate(vis):
            if not b:
                email_set = set()
                dfs(i)
                res.append([accounts[i][0]] + sorted(email_set))
        return res
