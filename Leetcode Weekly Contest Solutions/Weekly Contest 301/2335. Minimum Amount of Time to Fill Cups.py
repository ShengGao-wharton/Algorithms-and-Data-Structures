class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0
        amount.sort()
        if amount[0] == amount[1] == 0:
            return amount[2]
        while sum(amount) > 0:
            amount.sort()
            if amount[0] > 0:
                amount[0] -= 1
                amount[2] -=1
            elif amount[1] > 0:
                amount[1] -= 1
                amount[2] -= 1
            else:
                return res + amount[2]
            res += 1
        return res