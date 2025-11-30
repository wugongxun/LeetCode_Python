class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        suf_min = ['z'] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_min[i] = min(suf_min[i + 1], s[i])

        res = []
        st = []
        for i, ch in enumerate(s):
            st.append(ch)
            while st and st[-1] <= suf_min[i + 1]:
                res.append(st.pop())
        return ''.join(res)
