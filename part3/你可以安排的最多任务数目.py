import bisect
from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            k += 1
            i, p = 0, pills
            valid_tasks = deque()
            for w in workers[-k:]:
                while i < k and tasks[i] <= w + strength:
                    valid_tasks.append(tasks[i])
                    i += 1
                if not len(valid_tasks):
                    return True
                if w >= valid_tasks[0]:
                    valid_tasks.popleft()
                    continue
                if p == 0:
                    return True
                p -= 1
                valid_tasks.pop()
            return False

        return bisect.bisect_left(range(min(len(tasks), len(workers))), True, key=check)
