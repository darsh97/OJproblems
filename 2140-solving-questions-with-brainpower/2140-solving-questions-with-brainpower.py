class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        @lru_cache(None)
        def dp(i: int) -> int:
            if i < n:
                pick = questions[i][0] + dp(i + questions[i][1] + 1)
                skip = dp(i + 1)
                return max(pick, skip)
            return 0

        return dp(0)

