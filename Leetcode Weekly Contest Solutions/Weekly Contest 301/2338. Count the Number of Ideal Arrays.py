# You are given two integers n and maxValue, which are used to describe an ideal array.
#
# A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
#
# Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
# Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
# Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        p = []

        for num in range(2, maxValue + 1):
            prime = True
            for i in range(2, int(math.sqrt(num)) + 1):
                if (num % i == 0):
                    prime = False
                    break
            if prime:
                p.append(num)
        m = len(p)
        d = defaultdict(list)
        for i in range(m):
            d[p[i]] = [0] * m
            d[p[i]][i] = 1
        # calculate prime factorization for each possible maxValue
        for v in range(3, maxValue + 1):
            if v not in d:
                d[v] = [0] * m
                for i in range(m):
                    prime = p[i]
                    if v % prime == 0:
                        d[v] = d[v // prime].copy()
                        d[v][i] += 1
                        break

        # calculate combinatorics number C(ri+n-1, n-1) to speed up (memorization)
        @lru_cache(None)
        def C(n, k):
            if k == 1:
                return n
            if k > n:
                return 0
            return C(n - 1, k) + C(n - 1, k - 1)

        N = 10 ** 9 + 7
        res = 0
        for v in range(1, maxValue + 1):
            r = d[v]
            t = 1
            for ri in r:
                if ri > 0:
                    t *= C(ri + n - 1, min(n - 1, ri))

            res += t % N
        return res % N