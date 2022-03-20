class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        directions = list(directions)
        cnt = 0

        for i in range(n - 1):
            if directions[i] == 'R' and directions[i + 1] == 'L':
                cnt += 2
                directions[i] = directions[i + 1] = 'S'

        for i in range(1, n):
            if directions[i - 1] == 'S' and directions[i] == 'L':
                directions[i] = 'S'
                cnt += 1

        directions.reverse()

        for i in range(1, n):
            if directions[i - 1] == 'S' and directions[i] == 'R':
                directions[i] = 'S'
                cnt += 1

        return cnt