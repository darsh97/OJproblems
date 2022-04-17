# How to add 2's and 3's to reach k?

def find_way(n):
    three_times = floor(n / 3)
    diff = n % 3

    if not diff:
        return three_times
    elif diff == 1:
        return (three_times - 1) + ((n - ((three_times - 1) * 3)) // 2)     
    else:
        return (three_times - 1) + ((n - ((three_times - 1) * 3)) // 2)


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        t = 0
        for k, v in cnt.items():
            if v == 1:
                return -1
            else:
                t += find_way(v)
        return t
