class Solution:
    def digitSum(self, s: str, k: int) -> str:
        ans = s
        n = len(s)
        while len(ans) > k:
            n = len(ans)
            new = ""
            i = 0
            while i <= n -1:
                curend = min(n, i + k)
                new = new + str(sum(int(a) for a in ans[i:curend]))
                i = curend
            ans = new
        return ans