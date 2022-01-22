class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        m: int = 0
        while target > 1:
            if target & 1:
                target -= 1
            else:
                if maxDoubles:
                    target //= 2
                    maxDoubles -= 1
                else:
                    break
            m += 1
        return m + (target - 1)