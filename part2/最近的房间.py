import bisect
from cmath import inf
from typing import List

from sortedcontainers import SortedList

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = [-1] * n
        rooms.sort(key=lambda room: room[1])
        j = len(rooms) - 1
        room_ids = SortedList()
        for i in sorted(range(n), key=lambda x: queries[x][1], reverse=True):
            preferred, min_size = queries[i]
            while j >= 0 and rooms[j][1] >= min_size:
                room_ids.add(rooms[j][0])
                j -= 1
            min_abs = inf
            idx = room_ids.bisect_left(preferred)
            if idx:
                min_abs = preferred - room_ids[idx - 1]
                res[i] = room_ids[idx - 1]
            if idx < len(room_ids) and room_ids[idx] - preferred < min_abs:
                res[i] = room_ids[idx]
        return res

print(Solution().closestRoom([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]]))

