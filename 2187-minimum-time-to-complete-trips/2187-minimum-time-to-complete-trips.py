class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lb = 0
        rb = max(time) * totalTrips

        min_time = None
        def get_trips(k) -> bool:
            return sum(k // t for t in time) >= totalTrips

        while lb <= rb:
            mb = lb + (rb - lb) // 2

            if get_trips(mb):
                min_time = mb
                rb = mb - 1

            else:
                lb = mb + 1

        return min_time