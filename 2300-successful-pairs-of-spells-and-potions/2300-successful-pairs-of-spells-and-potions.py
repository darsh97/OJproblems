class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []

        for s in spells:
            d = success / s
            res.append(n - bisect.bisect_left(potions, d))

        return res