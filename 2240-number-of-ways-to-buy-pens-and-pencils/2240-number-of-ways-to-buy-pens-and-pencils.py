class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        only_pens = floor(total / cost1)
        only_pencils = floor(total / cost2)

        mx_cost = max(cost1, cost2)
        mi_cost = min(cost1, cost2)

        res = only_pencils + only_pens + 1

        for k in range(1 , 1 + min(only_pens, only_pencils)):
            # if i buy k items of item with max cost, how much of min items can I buy?
            remaining = total - (k * mx_cost)
            res += remaining//mi_cost

        return res