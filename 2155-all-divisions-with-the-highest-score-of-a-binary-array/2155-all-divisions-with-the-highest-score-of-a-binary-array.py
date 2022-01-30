class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zero = 0
        one = sum(nums)
        res = [one, ]
        mx = res[0]

        for i in range(n):
            zero += not nums[i]
            one -= nums[i]
            res.append(zero + one)
            mx = max(mx, res[-1])

        return [i for i, e in enumerate(res) if e == mx]
