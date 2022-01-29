class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t = sum(nums)

        if t % 2:
            return False
        
        ht = t // 2

        @lru_cache(None)
        def dp(i, s):
            if i >= len(nums) or s > ht:
                return False

            if s == ht:
                return True

            return dp(i + 1, s + nums[i]) or dp(i + 1, s)

        return dp(0, 0)
