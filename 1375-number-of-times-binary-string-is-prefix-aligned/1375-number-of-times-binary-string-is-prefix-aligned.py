class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        last_one = -inf
        first_zero = 1
        cnt = 0
        for l in light:
            last_one = max(last_one, l)
            if first_zero >= last_one:
                cnt += 1
            first_zero += 1
        return cnt