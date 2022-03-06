class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        last_one = -inf
        first_zero = 1
        cnt = 0
        for l in light:
            last_one = max(last_one, l)
            cnt += first_zero >= last_one
            first_zero += 1
        return cnt