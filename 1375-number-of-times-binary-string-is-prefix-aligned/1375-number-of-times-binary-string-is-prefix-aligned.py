class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        last_one = -inf
        zero_heap = [*range(1, len(light) + 1)]
        heapq.heapify(zero_heap)
        cnt = 0
        for l in light:
            first_zero = heapq.heappop(zero_heap)
            last_one = max(last_one, l)
            if first_zero >= last_one:
                cnt += 1
        return cnt