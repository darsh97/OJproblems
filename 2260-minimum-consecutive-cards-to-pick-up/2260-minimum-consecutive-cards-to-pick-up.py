inf = float("inf")

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = inf
        d = {}
        for i, e in enumerate(cards):
            if e in d:
                res = min(res, i - d[e] + 1) 
            d[e] = i
        
        return res if res != inf else -1
            