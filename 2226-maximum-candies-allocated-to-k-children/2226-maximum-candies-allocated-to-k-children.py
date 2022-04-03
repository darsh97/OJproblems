class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lb, rb = 1, sum(candies) // k
        res = 0

        def is_feasible(m):
            return sum(c // m for c in candies) >= k

        while lb <= rb:
            mb = lb + (rb - lb) // 2
            if is_feasible(mb):
                lb = mb + 1
                res = max(res, mb)
            else:
                rb = mb - 1
        return res