from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # 提前计算需要的阶乘
        fac = [factorial(i) for i in range(n + 1)]
        res = 0
        vis = set()
        # 只循环回文串的左半边，例如，12321 -> 只需要循环123即可
        # 例如n=5，从100循环到999
        base = 10 ** ((n - 1) // 2)
        for x in range(base, 10 * base):
            s = str(x)
            # 拼接回文串的右半边
            s += s[::-1][n % 2:]
            # 是否能整除k
            if int(s) % k:
                continue
            # 排序，判断是否已经计算过
            sorted_s = ''.join(sorted(s))
            if sorted_s in vis:
                continue
            vis.add(sorted_s)
            # 如果x中没有重复的数，以12345为例，可以排列组合得到的不同数为 5!
            # 如果x有重复的数，以12321为例，可以排列组合得到的不同数为 5! / (2! * 2!)，1出现两次，2出现两次
            # 可以推出长度为n的数的公式为 n! / (C0! * C1! * C2! * ... * C9!) ---> Ci表示i这个数字在这x中出现的次数
            # 如果x中有0的情况下，第一位不能为0，第一位的可能情况则为 n - C0，剩下的位数依旧是阶乘计算，为(n - 1)!
            # 综上，最后的公式为，(n - C0) * (n - 1)! / (C0! * C1! * C2! * ... * C9!)
            cnt = Counter(sorted_s)
            t = (n - cnt['0']) * fac[n - 1]
            for c in cnt.values():
                t //= fac[c]
            res += t
        return res



print(Solution().countGoodIntegers(5, 6))