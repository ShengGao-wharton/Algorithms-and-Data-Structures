# You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.
#
# A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.
#
# The product of a path is defined as the product of all the values in the path.
#
# Return the maximum number of trailing zeros in the product of a cornered path found in grid.
#
# Note:
#
# Horizontal movement means moving in either the left or right direction.
# Vertical movement means moving in either the up or down direction.

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def pow2(n):
            res = 0
            while n % 2 == 0:
                res += 1
                n //= 2
            return res

        def pow5(n):
            res = 0
            while n % 5 == 0:
                res += 1
                n //= 5
            return res

        m, n = len(grid), len(grid[0])
        two = [[0] * n for _ in range(m)]
        five = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                two[i][j] = pow2(grid[i][j])
        for i in range(m):
            for j in range(n):
                five[i][j] = pow5(grid[i][j])
        twoup = [[0] * n for _ in range(m)]
        twodown = [[0] * n for _ in range(m)]
        twoleft = [[0] * n for _ in range(m)]
        tworight = [[0] * n for _ in range(m)]
        fiveup = [[0] * n for _ in range(m)]
        fivedown = [[0] * n for _ in range(m)]
        fiveleft = [[0] * n for _ in range(m)]
        fiveright = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if i == 0:
                    twoup[i][j] = two[i][j]
                else:
                    twoup[i][j] = two[i][j] + twoup[i - 1][j]

        for j in range(n):
            for i in range(m - 1, -1, -1):
                if i == m - 1:
                    twodown[i][j] = two[i][j]
                else:
                    twodown[i][j] = two[i][j] + twodown[i + 1][j]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    twoleft[i][j] = two[i][j]
                else:
                    twoleft[i][j] = two[i][j] + twoleft[i][j - 1]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    tworight[i][j] = two[i][j]
                else:
                    tworight[i][j] = two[i][j] + tworight[i][j + 1]

        # calculate five
        for j in range(n):
            for i in range(m):
                if i == 0:
                    fiveup[i][j] = five[i][j]
                else:
                    fiveup[i][j] = five[i][j] + fiveup[i - 1][j]

        for j in range(n):
            for i in range(m - 1, -1, -1):
                if i == m - 1:
                    fivedown[i][j] = five[i][j]
                else:
                    fivedown[i][j] = five[i][j] + fivedown[i + 1][j]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    fiveleft[i][j] = five[i][j]
                else:
                    fiveleft[i][j] = five[i][j] + fiveleft[i][j - 1]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    fiveright[i][j] = five[i][j]
                else:
                    fiveright[i][j] = five[i][j] + fiveright[i][j + 1]

        ans = 0
        for i in range(m):
            for j in range(n):
                leftdown = min(twoleft[i][j] + twodown[i][j] - two[i][j], fiveleft[i][j] + fivedown[i][j] - five[i][j])
                rightdown = min(tworight[i][j] + twodown[i][j] - two[i][j],
                                fiveright[i][j] + fivedown[i][j] - five[i][j])
                leftup = min(twoleft[i][j] + twoup[i][j] - two[i][j], fiveleft[i][j] + fiveup[i][j] - five[i][j])
                rightup = min(tworight[i][j] + twoup[i][j] - two[i][j], fiveright[i][j] + fiveup[i][j] - five[i][j])
                ans = max(leftdown, ans, leftup, rightup, rightdown)

        return ans
