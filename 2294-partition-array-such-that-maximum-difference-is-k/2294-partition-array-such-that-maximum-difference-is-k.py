class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r = c = 0

        while r < len(nums):
            while r < len(nums) and (nums[r] - nums[l]) <= k:
                r += 1
            else:
                c += 1
                l = r

        return c