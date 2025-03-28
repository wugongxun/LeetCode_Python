from typing import List


class Solution:
    # 可以使用Kruskal算法，求出最小生成树
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        res = 0
        # h: 水平切的次数，v: 垂直切的次数
        h = v = 1
        while horizontalCut or verticalCut:
            # 先切一刀，需要在另一个方向需要切两刀，所以优先切开销大的
            # not horizontalCut: 以及不能再水平切了，verticalCut and verticalCut[-1] < horizontalCut[-1]: 还可以垂直切，并且垂直切的开销大于水平切
            if not horizontalCut or (verticalCut and verticalCut[-1] > horizontalCut[-1]):
                # 垂直切
                res += verticalCut.pop() * v
                h += 1
            else:
                # 水平切
                res += horizontalCut.pop() * h
                v += 1
        return res

print(Solution().minimumCost(3, 2, [1, 3], [5]))