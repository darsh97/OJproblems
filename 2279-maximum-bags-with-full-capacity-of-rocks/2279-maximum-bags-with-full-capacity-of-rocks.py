
class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:

        capacity_left = sorted((c - r) for i, (c, r) in enumerate(zip(capacity, rocks)))
        res = 0

        for cl in capacity_left:
            if not cl:
                res += 1
            else:
                if cl <= additionalRocks:
                    res += 1
                    additionalRocks -= cl
                else:
                    return res
        return res